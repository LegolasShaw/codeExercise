from multiprocessing import Pool
import time
import os

from flask import Flask



def func(msg):
    while True:
        print(msg)
        time.sleep(5)

msg = 'i am child process 1'


msg2 = 'i am child process 2'
app = Flask(__name__)
pid = os.fork()

if pid == 0:
    func(msg)

pid = os.fork()
if pid == 0:
    func(msg2)





#
#
# pool = Pool(processes=1)
#

# pool.apply_async(func, (msg, ))
#
#
