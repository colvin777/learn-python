'''
Created on 

@author: haoweizh
'''

class classic:                                                                 
    def __getattr__(self, name):                                               
        if name == 'age':                                                      
            return 40                                                          
        else:                                                                  
            raise AttributeError                                               
                                                                               
x = classic()                                                                  
x.age                                 # Runs __getattr__                       
                                                                               
#x.name                                # Runs __getattr__                       
                                                                               
                                                                               
                                                                               
class newprops(object):                                                        
    def getage(self):                                                          
        return 40                                                              
    age = property(getage, None, None, None)  # get, set, del, docs            
                                                                               
x = newprops()                                                                 
x.age  
                                                                               
#x.name                                        # Normal fetch                   
                                                                               
                                                                               
                                                                               
class newprops2(object):                                                        
    def getage(self):                                                          
        return 40                                                              
    def setage(self, value):                                                   
        print('set age:', value)                                               
        self._age = value                                                      
    age = property(getage, setage, None, None)                                 
                                                                               
x = newprops2()                                                                 
y = newprops2()                                                                               
x.age = 42                                    # Runs setage                    
print(x.age)                                 # Normal fetch; no getage call   
y.age = 11
print(x.age)
print(x._age)                                                                               
x.job = 'trainer'                             # Normal assign; no setage call  
x.job                                         # Normal fetch; no getage call   
                                                                               
print(newprops2.__dict__)                                                                           
print(x.__dict__)  

                                                                                
class classic2:                                                                 
    def __getattr__(self, name):              # On undefined reference         
        if name == 'age':                                                      
            return 40                                                          
        else:                                                                  
            raise AttributeError                                               
    def __setattr__(self, name, value):       # On all assignments             
        print('set:', name, value)                                             
        if name == 'age':                                                      
            self.__dict__['_age'] = value                                      
        else:                                                                  
            self.__dict__[name] = value                                        
                                                                               
x = classic2()                                                                  
x.age                                         # Runs __getattr__               
                                                                               
x.age = 41                                    # Runs __setattr__               
print(x._age)                                        # Defined: no __getattr__ call   
                                                                               
x.job = 'trainer'                             # Runs __setattr__ again         
x.job                                         # Defined: no __getattr__ call   
