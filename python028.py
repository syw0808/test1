import sys

def comp1(seq: str) -> str:
    comp=""
    for s in seq:
        if s=="A":
            comp+="T"
        elif s=="C":
            comp+="G"
        elif s=="G":
            comp+="C"
        elif s=="T":
            comp+='A'    
    return comp
        
def comp2(seq:str)->str:
    d_comp={'A':'T','T':'A','G':'C','C':'G'}
    comp=""
    for s in seq:
        comp+=d_comp[s]
    return comp

if __name__ == "__main__" :#! 외부에서 import 하면 실행 안됨
    if len(sys.argv)!=2:
        print(f"usage : python {sys.argv[0]} [string]")
        sys.exit()

    seq=sys.argv[1]
    c1=comp1(seq)
    c2=comp2(seq)
    print(c1)
    print(c2)

print("Hi")

