'''
Created on 

@author: haoweizh
'''
import os
import sys

class envTool():
    #__slots__ = ['python', 'pyang']
    def __init__(self):pass
    
    def __setattr__(self, attr, value):
        if (attr == 'python'):
            if(value == '' or not os.path.exists(value)):
                self.__dict__['python'] = os.environ.get("PATH_TO_CONVERT2YANG_PYTHON") if \
                os.environ.get('PATH_TO_CONVERT2YANG_PYTHON') is not None \
                  else sys.executable
            else:
                self.__dict__['python'] = value
        elif (attr == 'pyang'):
            if(value == '' or not os.path.exists(value)):
                self.__dict__['pyang'] = os.environ.get('PYANGPATH') if \
                os.environ.get('PYANGPATH') is not None else False
                assert self.__dict__['pyang'] is not False, "could not find path to pyang"
            else:
                self.__dict__['pyang'] = value
        elif (attr == 'libPathDir'):
            if(value == '' or not os.path.exists(value)):
                self.__dict__['libPathDir'] = os.environ.get('YANG_MODPATH') if \
                os.environ.get('YANG_MODPATH') is not None else False
                assert self.__dict__['libPathDir'] is not False, "could not find lib yang path to pyang"
            else:
                self.__dict__['libPathDir'] = value
        elif (attr == 'xslPathDir'):
            if(value == '' or not os.path.exists(value)):
                self.__dict__['xslPathDir'] = os.environ.get('XSL_PATH') if \
                os.environ.get('XSL_PATH') is not None else False
                assert self.__dict__['xslPathDir'] is not False, "could not find XSL template path to pyang"
            else:
                self.__dict__['xslPathDir'] = value
    def __getattribute__(self, name):
        return object.__getattribute__(self, name)
        #return getattr(self, name)
        #return self.__dict__[name]
        
en =envTool()
en.python = 'fasd'
print(en.python)