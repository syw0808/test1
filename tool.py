#! /usr/bin/env python
import sys


class FASTA:
    def __init__(self, file_name:str):
        self.file_name=file_name
        self.count= {}
        self.length=0
    def count_base(self):
        with open(self.file_name, 'r') as handle:
            for line in handle:
                if line.startswith(">"):
                    continue
                for s in line.strip():
                    if s in self.count :
                        self.count[s]+=1
                    else:
                        self.count[s]=1

    def get_length(self):

        for k, v in self.count.items():
            self.length+=v

    def __len__(self):
        self.get_length()
        return self.length

class FASTQ:
    def __init__ (self, file_name:str):
        self.file_name=file_name
        self.read_num=0
        self.base={}
        self.length=0

    def count_read_num(self):
        cnt=0
        with open(self.file_name,'r') as handle:
            for line in handle:
                if cnt%4==0:
                    header = line.strip()
                    self.read_num+=1
                elif cnt%4==1:
                    seq = line.strip()
                    self.count_base(seq)
                elif cnt%4==3:
                    qual = line.strip()
                cnt+=1
                
    def count_base(self, seq:str): #count_read_num에서 호출됨
        for base in seq :
            if base in self.base:
                self.base[base]+=1
            else :  
                self.base[base]=1
    def count_length(self):
        for k, v in self.base.items():
            self.length+=v



if __name__ == "__main__":
    if len(sys.argv)!=2:
        print(f"usage : python :{sys.argv[0]} [fasta]")
        sys.exit()
    file_name = sys.argv[1]
    """
    t = FASTA(file_name)
    t.count_base()
    print(t.count)
    t.get_length()
#    print(t.length)
#    print(len(t)) #python 기본 함수를 인스턴스에도 적용 가능
 """
    tq = FASTQ(file_name)
    tq.count_read_num()
    print(f"read 수 :{tq.read_num}")
    print(f"base 수 :{tq.base}")
    tq.count_length()
    print(f"길이 :{tq.length}")
