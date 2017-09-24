'''
Created on 

@author: colvin
'''
from multiprocessing import Pool                                                  
import time                                                                       
                                                                                  
def foo(n):                                                                       
    print(n)                                                                      
#     time.sleep(1)                                                                 
                                                                                  
if __name__ == '__main__':                                                        
    pool_obj=Pool(5)    #                                                         
    for i in range(47):                                                           
        # pool_obj.apply_async(func=foo,args=(i,))                                
        pool_obj.apply_async(func=foo,args=(i,))   
        # apply                                             
        # apply_async                                 
    pool_obj.close()                                                              
    pool_obj.join()                                                               
    print('ending')                                                               
