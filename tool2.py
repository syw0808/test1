#! /usr/bin/env python
import sys

class FASTA:
    def __init__(self, file_name:str):
        self.file_name = file_name
        self.count={}
        self.length=0
    def count_base(self):
        with open(self.file_name, 'r') as handle :
            for line in handle:
                if line.startswith('>'):
                    continue
                for s in line.strip():
                    if s in self.count :
                        self.count[s]+=1
                    else :
                        self.count[s]=1 
    
    def get_length(self):
        for k, v in self.count.items():
            self.length+=v

class FASTQ:
    def __init__(self, file_name:str):
        self.file_name=file_name
        self.read_num=0
        self.seq=''

    def count_read_num(self):
        cnt=0
        with open(self.file_name, 'r') as handle:
            for line in handle:
                if cnt%4==0:
                    header = line.strip()
                    self.read_num+=1
                    cnt+=1
                elif cnt%4==1:
                    cnt+=1
                    self.seq+=line.strip()
                elif cnt%4==2:
                    cnt+=1
                elif cnt%4==3:
                    cnt+=1
    def count_length(self):
        return len(self.seq) 
    
        
           



 

f1 = FASTA("059.fasta")
f1.count_base()
print(f1.count)
f1.get_length()
print(f1.length)

f2=FASTQ("061.fastq")
f2.count_read_num()
print(f2.read_num)
print(f2.seq)
print(len(f2.seq))
f2Len=f2.count_length()
print(f2Len)

