'''
Created on 

@author: colvin
'''
from multiprocessing import Process,Pipe

import time,os                                               
def consumer(p,name):                                        
    left,right=p                                             
    left.close()                                             
    while True:                                              
        try:                                                 
            baozi=right.recv()                               
            print('%s receive:%s' %(name,baozi))            
        except EOFError as e:
            print(repr(e))                                     
            right.close()                                    
            break                                            
def producer(seq,p):                                         
    left,right=p                                             
    right.close()                                            
    for i in seq:                                            
        left.send(i)                                         
        # time.sleep(1)                                      
    else:                                                    
        left.close()                                         
if __name__ == '__main__':                                   
    left,right=Pipe()                                        
    c1=Process(target=consumer,args=((left,right),'c1'))     
    c1.start()                                               
    seq=(i for i in range(10))                               
    producer(seq,(left,right))                               
    right.close()                                            
    left.close()                                             
    c1.join()                                                
    print('main process')                                          
