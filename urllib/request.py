# -*- coding: utf-8 -*-   
###########colvin  coding=gbk
'''
Created on 

@author: haoweizh
'''
import urllib.request
import sys

# proxies = {'http': 'http://135.245.48.34:8000/', 'https': 'https://135.245.48.34:8000/', 'ftp': 'ftp://135.245.48.34:8000/'}
# opener = urllib.request.FancyURLopener(proxies)
# with opener.open("http://www.python.org") as f:
#     f.read().decode('utf-8')

type1 = sys.getfilesystemencoding()
type2 = sys.getdefaultencoding()
print(type1, type2)
proxy_handler = urllib.request.ProxyHandler({'http': 'http://135.245.48.34:8000/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
 
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
# This time, rather than install the OpenerDirector, we use it directly:
#http://1.hd.mi.com/detail?pid=88058798008989&product_id=2170800024
f = opener.open('http://www.baidu.com')
print(f.read().decode('utf-8').encode(type1))

                           
                                                     
# import re                                            
# import sys                                           
#                                                      
# import urllib                                        
# sys.setdefaultencoding('utf-8')                      
# type = sys.getfilesystemencoding()                   
# r = urllib.urlopen("http://www.baidu.com")           
# a = r.read().decode('utf-8').encode(type)            
# print (a)                                              
