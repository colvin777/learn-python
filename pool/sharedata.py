'''
Created on 
@author: colvin
'''
from multiprocessing import Manager,Process                                                     
def foo(l,i):  
    print(i*i)                                                                                 
    l.append(i*i)                                                                              
if __name__ == '__main__':                                                                      
    man=Manager()                                                                               
    ml=man.list([11,22,33])                                                                     
    l=[]                                                                                        
    for i in [1,2,3,4,5]:                                                                          
        p=Process(target=foo,args=(ml,i))                                                       
        p.start()                                                                               
        l.append(p)                                                                             
    for i in l: #  
        i.join()                                                                                
    print(ml)                                                                                   
