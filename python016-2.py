#! /usr/bin/env python
import sys
import gzip

if len(sys.argv) != 2:
    print(f"#usage : python {sys.argv[0]} [fasta]")
    sys.exit()

f= sys.argv[1]
dic={}
with gzip.open(f,'rb') as handle :
    for line in handle:
        line=line.decode("utf-8").strip()
        if line.startswith(">"):
            continue
        for s in line:
            if s in dic :
                dic[s]+=1
            else : dic[s]=1
        
with open("result1.txt","w") as handle:
    handle.write(f"A: {dic['A']}\n")
    handle.write(f"T: {dic['T']}\n")
    handle.write(f"G: {dic['G']}\n")
    handle.write(f"C: {dic['C']}\n")
print(dic)
length=0
for k, v in dic.items():
    length+=v

print(length)

sys.exit()
