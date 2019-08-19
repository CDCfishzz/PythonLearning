# -*- coding: utf-8 -*-
# 分布式进程
# task_worker
import sys
import time
import queue
from multiprocessing.managers import BaseManager


# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass


# 由于这两个QueueManager只从网络上获取Queue,所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器,也就是运行task_master的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)

# 端口和验证码与master保持一致:
m = QueueManager(address=('', 5000), authkey=b'abc')
# 从网络连接:
m.connect()

# 获取通过网络访问的Queue对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列获取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)

# 关闭:
manager.shutdown()
print('master exit.')
