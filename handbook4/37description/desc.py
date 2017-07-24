'''
Created on 

@author: haoweizh
'''
class Descriptor(object):                                                   
    def __get__(self, instance, owner):                                     
        print(self, instance, owner, sep='\n')                              
                                                                            
class Subject:                                                              
    attr = Descriptor()             # Decriptor instance is class attr      
                                                                            
X = Subject()                                                               
                                                                            
X.attr                                                                      
