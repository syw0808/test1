#! /usr/bin/env python
import sys

f=sys.argv[1]
l=list()
dic={}
def readcsv(filename):
    ret=list()
    with open(f,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header=line.lstrip("#").strip().split(',')
                continue
            splitted=line.strip().split(',')
            d=dict(zip(header, splitted))
            ret.append(d)
    return ret
            
if __name__ == "__main__":
    if len(sys.argv)!=2:
        print(f"usage : python {sys.argv[0]} [txt]")
res=  readcsv(f)
print(res)

                
                    


readcsv(f)
