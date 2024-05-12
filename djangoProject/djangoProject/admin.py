from django.contrib import admin
from .models import Script, VirtualMachine


@admin.register(Script)
class ScriptAdmin(admin.ModelAdmin):
    pass


@admin.register(VirtualMachine)
class VirtualMachineAdmin(admin.ModelAdmin):
    pass
