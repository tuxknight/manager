.. _README:
=========
Manager
=========

基于 `django`_ 框架，使用 `sqlite`_ 进行持久化存储，后台使用 `ansible`_ 对远程主机执行指令。

.. _django: http://www.djangoproject.com/
.. _sqlite: http://www.www.sqlite.org/
.. _ansible: http://www.ansible.com/

功能
=======

  * 查看设备列表，包括设备名称、序列化、IP地址、登录名、密码、备注等信息。其中，登录名和密码可用于ansible执行命令时的ssh认证。

  * 添加设备，根据填写设备的相关信息添加设备。

  * 设备管理，利用表单提交ansible操作指令。可在Model(Modules)里添加允许通过调用的模块。后台利用 ``ansible.runner.Runner`` 和 ``ansible.inventory.Inventory`` 类来调用ansible的相关模块。

  * 操作日志，添加设备、执行命令的操作会作为操作日志记录下来以留做审计等用途。

自定义模块
============

 ``miss`` 为自定义模块，功能为获取应用miss的日志信息，包括版本号、运行时长、会话数、当前流量、最大流量等信息。

支持的选项::

  options:
    info:
      required: true
      choices: [ version, uptime, session, flowrate, maxflowrate ]

示例::

  # return the version of miss.out
  - miss: info=version

  # return current session count
  - miss: info=session


miss 的日志格式为::

  ********* MISSv5.0_x64_20150310_Shanghai************************
  uptime: 2h 32min 32s
  current sessions count: 300213 max sessions count: 6772382
  current flowrate: 524[Mbps] max flowrate: 634[Mbps]
  
  -------- protocol -----------------
            recv          send
  HTTP POST [23234242]   [23234242]
  HTTP GET  [99274242]   [99274242]
  SMTP      [23234242]   [23234242]
  
  ********* MISSv5.0_x64_20150310_Shanghai************************
  uptime: 2h 32min 37s
  current sessions count: 300213 max sessions count: 6772382
  current flowrate: 524[Mbps] max flowrate: 634[Mbps]
  
  -------- protocol -----------------
            recv          send
  HTTP POST [23234242]   [23234242]
  HTTP GET  [99274242]   [99274242]
  SMTP      [23234242]   [23234242]


miss 应用程序的目录树为::

     miss
     ├── bin
     │   └── miss.out
     ├── config
     │   ├── city.ini
     │   ├── http_post_white.ini
     │   ├── miss.ini
     │   ├── vest.ini
     │   └── voip.ini
     ├── logs
     │   ├── miss.py
     │   ├── missRunning.log
     │   ├── run.log
     │   └── tsl.log
     └── shell
         ├── missMaintainer.sh
             ├── missMonitor.sh
                 ├── missStart.sh
                     └── missStop.sh
    

Demo
========

Demo 请访问 http://52.11.97.205:8080 

Demo应用部署在 ``AWS EC2`` 上，使用 ``uwsgi`` 提供http服务。

Django Administration 登录: admin/1917434419

AWS EC2 主机
  52.25.151.1 root/chufuyuan ec2-user/780280897
  52.11.97.205 root/chufuyuan ubuntu/chufuyuan
