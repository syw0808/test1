#! /usr/bin/env python
import sys


if len(sys.argv) != 2:
    print(f"usage : python {sys.argv[0]} [fasta]")
    sys.exit()


f=sys.argv[1]
dic={}

with open(f,"r") as handle :
    for line in handle :
        if line.startswith(">"):
            continue
        for s in line.strip():
            if s in dic:
                dic[s]+=1
            else :
                dic[s]=1
       
print(dic)
total=0
for k, v in dic.items():
    total+=v
print(total)

with open("result.txt","w") as handle:
    handle.write(f"A:{dic['A']}\n")
    handle.write(f"C:{dic['C']}\n")
    handle.write(f"G:{dic['G']}\n")
    handle.write(f"T:{dic['T']}\n")

try :
    with open(f,'r') as handle:
        read=handle.readlines() #리스트로 반환

except FileNotFoundError :
    print(f"{f} not found.. please check..")
    sys.exit()

