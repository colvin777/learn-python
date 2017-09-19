'''
Created on Sep 13, 2017

@author: root
'''


from pymemcache.client.base import Client

client = Client(('135.251.217.42', 51432))
client.set('some_key', 'some_value')
result = client.get('some_key')
