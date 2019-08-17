# -*- coding: utf-8 -*-
import os
import random
import time
import subprocess
from multiprocessing import Process, Pool


def run_proc(name):
    print('Run child process %s(%s)...' % (name, os.getpid()))


def long_time_task(name):
    print('run task %s(%s)...' % (name, os.getppid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

    p2 = Pool(4)
    for i in range(5):
        p2.apply_async(long_time_task, args=(1,))
    print('Waiting for all subprocesses done...')
    p2.close()
    p2.join()
    print('All subprocesses done.')

    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)


