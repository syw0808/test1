#! /usr/bin/env python
import sys

f = sys.argv[1]
dic={}

with open(f,'r') as handle :
    for line in handle:
        if line.startswith(">") : continue
        for base in line.rstrip() :
            if base in dic:
                dic[base]+=1
            else : 
                dic[base]=1

total = 0
for k, v in dic.items():
    total+= v
print(total)
