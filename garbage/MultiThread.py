

from threading import Thread
import time

def den2():
    while True:
        print('Bat den 2' )
        time.sleep(3)
        print('Tat den 2')
        time.sleep(3)

def den3():
    while True:
        print('Bat den 3')
        time.sleep(4)
        print('Tat den 3')
        time.sleep(4)

dent2 = Thread(target = den2)
dent2.start()

dent3 = Thread(target = den3)
dent3.start()
while True:
    print('Bat den 1')
    time.sleep(2)
    print('Tat den 1')
    time.sleep(2)