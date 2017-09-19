'''
Created on 

@author: haoweizh
'''
class Indexer:                                                             
    data = [5, 6, 7, 8, 9]                                                 
    def __getitem__(self, index):   # Called for index or slice            
        print('getitem:', index)                                           
        return self.data[index]     # Perform index or slice               
                                                                           
X = Indexer()
                                                               
ret = "return {0}".format(X[0])                                # Indexing sends __getitem__ an integer
print(ret)

class Squares:                                                              
    def __init__(self, start, stop):    # Save state when created           
        self.value = start - 1                                              
        self.stop  = stop                                                   
    def __iter__(self):                 # Get iterator object on iter()     
        return self                                                         
    def __next__(self):                 # Return a square on each iteration 
        if self.value == self.stop:     # Also called by next() built-in    
            raise StopIteration                                             
        self.value += 1                                                     
        return self.value ** 2   
                                               
for i in Squares(1, 5):
    print(i, end=' ')  
