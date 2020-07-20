#! /usr/bin/env python

def factorial(n):
    res=1
    while n>1:
        res*=n
        n-=1
    return res

fac=factorial(5)
print(fac)
