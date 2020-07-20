#! /usr/bin/env python

for j in range(1,10):
    for i in range(2,10,2):
        print("%d*%d=%2d"%(i,j,i*j), end="   ")
    print() 
