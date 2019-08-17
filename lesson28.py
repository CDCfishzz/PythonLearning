# -*- coding: utf-8 -*-
# 进程之间的通信
import os
import random
import time
from multiprocessing import Process, Queue


# 写数据进程执行的代码:
def write(q1):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q1.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q1):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q1.get(True)
        print('Get %s from queue' % value)


if __name__ == '__main__':
    # 父进程创建Queue, 并传给各个子进程:
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw, 写入:
    pw.start()
    # 启动子进程pr, 读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程是死循环,只能强行终止:
    pr.terminate()
