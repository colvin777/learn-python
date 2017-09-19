'''
Created on 

@author: haoweizh
'''
from macpath import sep

def gen():
    yield 20
    print('*' * 20)
    yield 30
    #return 40

x = gen()
print(next(x))
print(x.send(33))
print(x)
#print(next(x) )

def gens():
    for i in range(10):
        x = (yield i) + 2
        print(x)
y = gens()
print(next(y))
print(y.send(2))
print(y.send(20))

def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        print(args)
        res.append(func(*args))
    return res

print(mymap(pow, [1,2,3], [2,3,4,5]))
