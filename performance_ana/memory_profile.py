#coding=GBK
'''
Created on 2017��10��9��

@author: haoweizh
'''
import random


@profile
def random_sort2(n):
    l = [random.random() for i in range(n)]
    l.sort()
    return l


if __name__ == "__main__":
    random_sort2(2000000)
