'''
Created on 

@author: haoweizh
'''
'''
    LEGB
    B -- import __builtin__
'''
g = 99                   # Global scope name: not used

def f1():
    g = 88               # Enclosing def local
    def f2():
        g  = 9
        def f3():
            global g
            print("in f3 %d", g)
        print("in f2 %d", g) 
        f3()      
    f2()
    print("in f1 %d", g)
f1()   
print("in global %d", g)                  # Prints 88: enclosing def local
print('===================================================================')
def makeActions():                                                       
    acts = []
    actc = []                                                            
    for i in range(5):                       # Tries to remember each i  
        acts.append(lambda x: i ** x)        # All remember same last i! 
    for i in range(5):                       # Tries to remember each i  
        actc.append(lambda x, i=i: i ** x)
    return acts, actc                                                         
                                                                         
acts, actc= makeActions()                                                     
print(acts[0](2))        
print(acts[3](2))    
print(actc[0](2))
print(actc[1](2))
print(actc[2](2,3))    

def tester(start):                                                        
    def nested(label):                                                    
        print(label, nested.state)      # nested is in enclosing scope    
        nested.state += 1               # Change attr, not nested itself  
    nested.state = start                # Initial state after func defined
    return nested                                                         
F = tester(0)                                                             
F('spam')            # F is a 'nested' with state attached                
F('ham')                                                                  
F.state              # Can access state outside functions too             
G = tester(42)       # G has its own state, doesn't overwrite F's         
G('eggs')                                                                 
F('ham')                                                                  
                                                
