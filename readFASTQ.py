#! /usr/bin/env python
import sys

f=sys.argv[1]

class FASTQ:
    def __init__(self, file_name:str):
        self.file_name=file_name
        self.read_num=0
    def count_read_num(self):
        with open(self.file_name, 'r') as handle:
            for line in handle:
                cnt=0
                if cnt%4==0 :
                    

fq = FASTQ(f)
print(fq.read_num)

