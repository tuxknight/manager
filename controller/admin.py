from django.contrib import admin

# Register your models here.
from django.contrib import admin
from controller.models import Device, ManageLog, DeviceState, Modules

admin.site.register(Device)
admin.site.register(DeviceState)
admin.site.register(ManageLog)
admin.site.register(Modules)