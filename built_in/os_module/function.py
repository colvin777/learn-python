'''
Created on 

@author: haoweizh
'''
# Delete everything reachable from the directory named in "top",
# assuming there are no symbolic links.
# CAUTION:  This is dangerous!  For example, if top == '/', it
# could delete all your disk files.
import os

def search(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            print("this is file %s parent is %s" % (name, root))
            #os.remove(os.path.join(root, name))
        for name in dirs:
            print("this is dir %s parent is %s" % (name, root))
            #os.rmdir(os.path.join(root, name))

search('E:/DocAndMaterialOfCompany/YANG&NETCONF/7510-orignal-yang-files/yang-source')