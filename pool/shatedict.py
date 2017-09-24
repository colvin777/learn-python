'''
Created on 

@author: colvin
'''

from multiprocessing import Manager,Process                                                                         
def foo(d,k,v):                                                                                                     
    d[k]=v                                                                                                          
if __name__ == '__main__':                                                                                          
    man=Manager()                                                                                                   
    md=man.dict({'name':'bob'})                                                                                     
    l=[]                                                                                                            
    for i in range(5):                                                                                              
        p=Process(target=foo,args=(md,i,'a'))                                                                       
        p.start()                                                                                                   
        l.append(p)                                                                                                 
    for i in l:                    
        i.join()                                                                                                    
    print(md)                                                                                                       
