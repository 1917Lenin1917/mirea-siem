import paramiko
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

SCRIPT_OUTPUTS = {}

@csrf_exempt
def execute_script(request):
    if request.method == 'POST':
        script = request.POST.get('script')
        vm_ip = request.POST.get('vm_ip')
        vm_username = request.POST.get('vm_username')
        vm_password = request.POST.get('vm_password')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(vm_ip, username=vm_username, password=vm_password)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

        stdin, stdout, stderr = ssh.exec_command(script)
        output = stdout.read().decode('utf-8')
        ssh.close()
        script_id = len(SCRIPT_OUTPUTS) + 1
        SCRIPT_OUTPUTS[script_id] = output

        return JsonResponse({'status': 'success', 'script_id': script_id})
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
