'''
Created on 

@author: haoweizh
'''
from lxml import etree

root = etree.Element("root")
#print(root.tag)
root.append( etree.Element("child1") )
child2 = etree.SubElement(root, "child2")
child3 = etree.SubElement(root, "child3")
print(etree.tostring(root, pretty_print=True))
child = root[0]                                  
print(child.tag)                                 
                                                 
print(len(root))                                 
                                                 
                                                 
root.index(root[1]) # lxml.etree only!           
                                                 
                                                 
children = list(root)                            
                                                 
for child in root:                               
    print(child.tag)                             
print('-' * 20)                                               
root.insert(0, etree.Element("child0"))          
start = root[:1]                                 
end   = root[-1:]                                
                                                 
print(start[0].tag)                              
print(end[0].tag)                                
