'''
Created on 

@author: haoweizh
'''
from io import StringIO, BytesIO

from lxml import etree
from lxml.etree import XMLSyntaxError


xml = u'<a xmlns="test"><b xmlns="test">aaa</b></a>'
root = etree.fromstring(xml)
print(etree.tostring(root))

StringIO(xml)                                                         
tree = etree.parse(StringIO(xml))
print(etree.tostring(tree.getroot()))

parser = etree.XMLParser(ns_clean=True)
tree   = etree.parse(StringIO(xml), parser)
print(etree.tostring(tree.getroot()))

# import elementtree.ElementTree as ET
import xml.etree.ElementTree as ET
treeConutry = ET.parse("country_data.xml")

print('*'* 40)
print(type(treeConutry))
# print(etree.tostring(treeConutry))
s = treeConutry.write("country_data.xml")
print(type(s))
print('*'* 40)

parser = etree.XMLParser()
print(len(parser.error_log))

try:
    tree = etree.XML("<root>\n</b>", parser)  # doctest: +ELLIPSIS
except XMLSyntaxError as ob:
    print(ob)

print(len(parser.error_log))

class EchoTarget(object):                                        
    def start(self, tag, attrib):                                
        print("start %s %r" % (tag, dict(attrib)))               
    def end(self, tag):                                          
        print("end %s" % tag)                                    
    def data(self, data):                                        
        print("data %r" % data)                                  
    def comment(self, text):                                     
        print("comment %s" % text)                               
    def close(self):                                             
        print("close")                                           
        return "closed!"                                         
                                                                 
parser = etree.XMLParser(target = EchoTarget())                  
                                                                 
result = etree.XML("<element>some<!--comment-->text</element>",  
                   parser)   
                                    
print(result)

# result = etree.XML(etree.tostring(treeConutry),  
#                    parser)  

