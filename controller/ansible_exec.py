#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'alex'

import ansible.runner
import ansible.inventory
from controller.models import Device


def device_info(id):
    record = Device.objects.filter(id=id)[0]
    return record


class Executor():
    def __init__(self, host, module, arguments, loginname='root', password=None):
        """init class Executor
        takes three arguments: host module arguments"""
        self.host = host
        self.module = module
        self.arguments = arguments
        self.remote_user = loginname
        if loginname == 'root':
            self.remote_pass = None
        else:
            self.remote_pass = password
        self.invetory = ansible.inventory.Inventory(host_list=[self.host])


    def doExec(self):
        """exec command using ansible.running.Runner"""
        runner = ansible.runner.Runner(
            module_name=self.module,
            module_args=self.arguments,
            pattern=self.host,
            forks=10,
            remote_user=self.remote_user,
            remote_pass=self.remote_pass,
            inventory=self.invetory
        )
        result_data = runner.run()
        return result_data