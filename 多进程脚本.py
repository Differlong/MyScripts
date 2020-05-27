import time
from multiprocessing import Lock, Process, Pool
from multiprocessing.managers import  BaseManager
import os
import random


def function(d1, d2):
    a, b = d1, d2
    c = a + b
    for i in range(50000):
        tmp = b + c
        a = b
        b = c
        c = tmp
    return c

class Data(object):
    def __init__(self):
        self.data=[i for i in range(100)]
        self.name = "data"
    def genData(self):
        return random.sample(self.data, 2)

    def wasteTime(self):
        function(*self.genData())

class MyManager(BaseManager):
    pass

MyManager.register("Data", Data)

def manager2():
    m = MyManager()
    m.start()
    return m

def function2(data):
    data.wasteTime()


def test():
    start = time.time()
    manager = manager2()
    data = manager.Data()
    pool = Pool(2)
    for i in range(1000):
        pool.apply_async(function, args=data.genData())
    pool.close()
    pool.join()
    print("All subprocess done!")
    end = time.time()
    print("Time: ", end - start)

# 多进程的荣光。速度可以显著提升。除了这台垃圾电脑。
if __name__ == "__main__1":
    test()

# 单进程的对比测试。
if __name__ == "__main__2":
    start = time.time()
    data = Data()
    for i in range(1000):
        function(*data.genData())

    print("All subprocess done!")
    end = time.time()
    print("Time: ", end - start)

# 这种方案不合适，还是单线程在跑。
if __name__ == "__main__":
    start = time.time()
    manager = manager2()
    data = manager.Data()
    pool = Pool(4)
    for i in range(1000):
        pool.apply_async(function2, args=[data])
    pool.close()
    pool.join()
    print("All subprocess done!")
    end = time.time()
    print("Time: ", end - start)