#! /usr/bin/env python
import sys
def fib(n:int) -> int:
    if n==0: return 0
    if n==1: return 1
    else :
            return fib(n-1)+fib(n-2)

n = int(sys.argv[1])
print(fib(n))
