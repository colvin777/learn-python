'''
Created on 2017Äê6ÔÂ6ÈÕ

@author: haoweizh
'''
#!/usr/bin/env python
# encoding: utf-8
'''
code.convert2yang -- shortdesc

code.convert2yang is a description

It defines classes_and_methods

@author:     haoweizh

@copyright:  2017 nokia. All rights reserved.

@license:    license

@contact:    Haowei.a.Zhang@alcatel-sbell.com.cn
@deffield    updated: Updated
'''


import threading,traceback,sys  
  
class catchThreadExcpetion(threading.Thread): 
    '''The timer class is derived from the class threading.Thread'''  
    def __init__(self, funcName, *args):  
        threading.Thread.__init__(self)  
        self.args = args  
        self.funcName = funcName  
        self.exitcode = 0  
        self.exception = None  
        self.exc_traceback = ''  
      
    def run(self): 
        '''Overwrite run() method, put what you want the thread do here'''  
        try:  
            self._run()  
        except Exception as e:  
            print(e)
            self.exitcode = 1       
            self.exception = e  
            self.exc_traceback = ''.join(traceback.format_exception(*sys.exc_info()))
            raise e  
      
    def _run(self):  
        try:  
            self.funcName(*(self.args))   
        except Exception as e:  
            raise e   