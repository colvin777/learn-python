'''
Created on 

@author: haoweizh
'''
counter = [1, 2, 3, 4]

updater = []
for i in counter:
    updater.append(i + 10)
print(updater)

def inc(x): return x + 10
l = map(inc, counter)
print(type(l))
print(list(l))

print(list(map((lambda x: x + 10), counter)))

def mymap(func, seq):
    res = []
    for x in seq:
        res.append(func(x))
    return res
print(mymap(inc, counter))

print(list(map(pow, [1, 2, 3], [2, 3, 4])))
print(list(zip([1, 3],[2, 4], [3, 5, 9])))
print(list(zip([-2, -1, 0, 1, 2])))

def mymapt(func, *seq):
    res = []
    for args in zip(*seq):
        res.append(func(*args))
    return res
print(mymapt(pow, [1, 2, 3], [2, 3, 4]))
