from django.db import models

class VirtualMachine(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    ssh_username = models.CharField(max_length=100)
    ssh_password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
