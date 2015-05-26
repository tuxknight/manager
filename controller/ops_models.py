#!/usr/bin/env python
# -*- coding:utf-8 -*-
from controller.models import ManageLog
from controller.models import Device
import time
__author__ = 'alex'


def operate_log(information):
    log_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    action = information
    managelog = ManageLog()
    managelog.log_time = log_time
    managelog.action = action
    managelog.save()


def add_device(name, sn, ipaddr, login, password, notes):
    device = Device()
    device.name = name
    device.sn = sn
    device.ipaddr = ipaddr
    device.login = login
    device.password = password
    device.notes = notes
    device.save()