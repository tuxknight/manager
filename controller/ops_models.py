#!/usr/bin/env python
# -*- coding:utf-8 -*-
from controller.models import ManageLog
from controller.models import Device
from controller.models import Modules

import time
__author__ = 'alex'
'''
CRUD
'''


def operate_log(information):
    log_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    action = information
    managelog = ManageLog()
    managelog.log_time = log_time
    managelog.action = action
    managelog.save()


def add_device(name, sn, ipaddr, login, password, notes=''):
    device = Device()
    device.name = name
    device.sn = sn
    device.ipaddr = ipaddr
    device.login = login
    device.password = password
    device.notes = notes
    device.save()


def add_modules(name, keys='', values=''):
    module = Modules()
    module.name = name
    module.keys = keys
    module.values = values