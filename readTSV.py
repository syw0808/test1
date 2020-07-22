#! /usr/bin/env python
import sys
import jason
f=sys.argv[1]
l=list()
dic={}
def readtsv(filename):
    ret=list()
    with open(f,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header=line.lstrip("#").strip().split('\t')
                continue
            splitted=line.strip().split('\t')
            d=dict(zip(header, splitted))
            ret.append(d)
    return ret
          
def to_jason(l:list) -> None :
    with open("read_sample.jason",'w') as handle:
        json.dump(l,handle, indent=4)
  
if __name__ == "__main__":
    if len(sys.argv)!=2:
        print(f"usage : python {sys.argv[0]} [txt]")
        sys.exit()

res=  readcsv(f)
print(res)

                
                    


readcsv(f)
