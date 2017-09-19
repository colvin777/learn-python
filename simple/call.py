'''
Created on 

@author: haoweizh
'''
class Callback:
    def __init__(self, color):               # Class with state information
        self.color = color
    def changeColor(self):                   # A normal named method
        print('turn', self.color)

objects = Callback('blue')
objects.a = 'a'
cb = objects.changeColor                     # Registered event handler
cb()

import subprocess 
import sys
try:
    retcode = subprocess.call("mycmd" + " myarg", shell=True)
    if retcode < 0:
        print('8' * 30)
        print(sys.stderr.readlines())
#         print("Child was terminated by signal", -retcode, file=sys.stderr)
    else:
        print(sys.stderr.)
#         print("Child returned", retcode, file=sys.stderr)
except OSError as e:
    print(e)
#     print("Execution failed:", e, file=sys.stderr)





