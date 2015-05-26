from django.db import models

# Create your models here.

class Device(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=20)
    sn = models.CharField(max_length=30)
    ipaddr = models.CharField(max_length=15)
    login = models.CharField(max_length=15, default='root')
    password = models.CharField(max_length=50)
    notes = models.CharField(max_length=5000, blank=True)

class ManageLog(models.Model):
    log_time = models.DateTimeField()
    action = models.CharField(max_length=300)

class DeviceState(models.Model):
    name = models.CharField(max_length=20)
    sn = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    check_time = models.TimeField()

class Modules(models.Model):
    name = models.CharField(max_length=20)
    keys = models.CharField(max_length=10, blank=True)
    values = models.CharField(max_length=10, blank=True)

