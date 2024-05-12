import paramiko
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Script, VirtualMachine
from .serializers import ScriptSerializer, VirtualMachineSerializer

SCRIPT_OUTPUTS = {}


@csrf_exempt
def execute_script(request, vm_id):
    if request.method == 'POST':
        script = request.POST.get('script')
        vm_ip = request.POST.get('vm_ip')
        vm_username = request.POST.get('vm_username')
        vm_password = request.POST.get('vm_password')
        print(vm_id, script, vm_ip, vm_username, vm_password)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(vm_ip, username=vm_username, password=vm_password)
        except Exception as e:
            return JsonResponse(
                {'status': 'error', 'message': str(e), 'ip': vm_ip, 'username': vm_username, 'password': vm_password})

        stdin, stdout, stderr = ssh.exec_command(f'sudo -S ./scripts/script{script}')
        stdin.write(f'{vm_password}\n')
        stdin.flush()
        output = stdout.read().decode('utf-8').replace(f'[sudo] password for {vm_username}: ', '')
        error = stderr.read().decode('utf-8').replace(f'[sudo] password for {vm_username}: ', '')
        ssh.close()
        script_id = len(SCRIPT_OUTPUTS) + 1
        SCRIPT_OUTPUTS[script_id] = output

        return JsonResponse({'status': 'success', 'script_id': script_id, 'output': output, 'error': error})
    else:
        return JsonResponse({'status': 'error', 'message': 'Метод запроса не поддерживается'})


@csrf_exempt
def get_script_status(request):
    if request.method == 'POST':
        script_id = request.POST.get('script_id')
        if script_id in SCRIPT_OUTPUTS:
            output = SCRIPT_OUTPUTS[script_id]
            del SCRIPT_OUTPUTS[script_id]

            return JsonResponse({'status': 'success', 'script_id': script_id, 'output': output})
        else:
            return JsonResponse({'status': 'error', 'message': 'Скрипт с указанным ID не найден'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Метод запроса не поддерживается'})


class ScriptsView(ModelViewSet):
    queryset = Script.objects.all()
    serializer_class = ScriptSerializer


class VMView(ModelViewSet):
    queryset = VirtualMachine.objects.all()
    serializer_class = VirtualMachineSerializer

    @action(detail=True, methods=['post'])
    def execute_script(self, request, *args, **kwargs):
        script_id = request.data.get('script')
        obj: VirtualMachine = self.get_object()
        vm_ip = obj.ip_address
        vm_username = obj.ssh_username
        vm_password = obj.ssh_password
        script = obj.scripts.get(id=script_id).filename

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(vm_ip, username=vm_username, password=vm_password)
        except Exception as e:
            return JsonResponse(
                {'status': 'error', 'message': str(e), 'ip': vm_ip, 'username': vm_username, 'password': vm_password})

        stdin, stdout, stderr = ssh.exec_command(f'sudo -S ./scripts/{script}')
        stdin.write(f'{vm_password}\n')
        stdin.flush()
        output = stdout.read().decode('utf-8').replace(f'[sudo] password for {vm_username}: ', '')
        error = stderr.read().decode('utf-8').replace(f'[sudo] password for {vm_username}: ', '')
        ssh.close()
        script_id = len(SCRIPT_OUTPUTS) + 1
        SCRIPT_OUTPUTS[script_id] = output

        return JsonResponse({'status': 'success', 'script_id': script_id, 'output': output, 'error': error})
