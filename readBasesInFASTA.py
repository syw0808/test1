#! /usr/bin/env python

from Bio import SeqIO #Bio 패키지에서 SeqIO 라이브러리 import 

record = SeqIO.read("059.fasta", "fasta") #SeqIO의 read method 실행
# -> record 객체 생성 (dir(record)로 이용 가능한 함수 확인)

A = record.seq.count("A") #record.seq <- 속성에 대하여 count method 실행
C = record.seq.count("C")
G = record.seq.count("G")
T = record.seq.count("T")

print(record.description) #header 저장되어 있
print(f"A:{A}")
print(f"C:{C}")
print(f"G:{G}")
print(f"T:{T}")
