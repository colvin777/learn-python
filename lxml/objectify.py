'''
Created on 

@author: haoweizh
'''
from lxml import etree
from lxml import objectify
from BeautifulSoup import BeautifulSoup

xml = '''<a xmlns="test"><b xmlns="test"><name>colvin</name><name>haowei</name></b></a>'''
root = etree.fromstring(xml)
print(etree.tostring(root))
newKid = etree.Element('c-1', laugh="Hi!")
root.insert(0, newKid)
print(newKid.getparent())
print(etree.tostring(root))
newKid.clear()
print(etree.tostring(root))
root.remove(newKid)
print(etree.tostring(root))

expr = "//*[local-name() = $name]"  
print([node for node in root.xpath(expr, name = "name")])
print(root.xpath(expr, name = "name")[0].tag) 
#print(root.index(root.xpath(expr, name = "name")[0])) 

soup = BeautifulSoup(xml,"lxml")

root = objectify.Element("root")
b = objectify.SubElement(root, "b")
print(root.b[0].tag)
del root.b
b = objectify.SubElement(root, "b")
print(root.b[0].tag)