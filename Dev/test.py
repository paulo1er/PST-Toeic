from threading import Thread
from time import sleep

def function01(arg,name):
    for i in range(arg):
        print(name,'i---->',i,"arg---->",arg,'\n')
        sleep(1)


def test01():
    thread1 = Thread(target = function01, args = (10,'thread1', ))
    thread1.start()
    sleep(1)
    thread2 = Thread(target = function01, args = (10,'thread2', ))
    thread2.start()
    thread1.join()
    print ("thread finished...exiting")



test01()
