#! /usr/bin/env python
ls = [3,1,1,2,0,0,2,3,3]

print(max(ls))
print(min(ls))

d={}

for i in ls:
    if i in d :
        d[i]+=1
    else: 
        d[i]=1

print(d)
