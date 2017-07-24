'''
Created on 

@author: haoweizh
'''

def myzip(*seqs):
    print(seqs)
    seqs = [list(S) for S in seqs]
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res
    
print(myzip([1, 2, 3], [2, 3, 4]))