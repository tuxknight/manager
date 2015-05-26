#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'alex'

import ansible.runner

class Executor():
    def __init__(self, host, module, arguments):
        '''init class Executor
        takes three arguments: host module arguments'''
        self.host = host
        self.module = module
        self.arguments = arguments

    def doExec(self):
        '''exec command using ansible.running.Runner'''
        runner = ansible.runner.Runner(
            module_name=self.module,
            module_args=self.arguments,
            pattern=self.host,
            forks=10
        )
        result_data = runner.run()
        return result_data