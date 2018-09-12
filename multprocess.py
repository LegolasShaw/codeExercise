from multiprocessing import Pool
import time
import os

from flask import Flask



def func(msg):
    while True:
        print(msg)
        time.sleep(5)

msg = 'i am child process'

app = Flask(__name__)
pid = os.fork()

if pid == 0:
    func(msg)





#
#
# pool = Pool(processes=1)
#

# pool.apply_async(func, (msg, ))
#
#
