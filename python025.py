#! /usr/bin/env python
Seq1="ATGTTATAG"

for s in Seq1[::3]:
    print(s,end=" ")

print()
#026
for i in range(0,len(Seq1),3):
    print(Seq1[i:i+3])

#027
for i in range(-1,-len(Seq1)-1,-1):
    print(Seq1[i], end='')
print()
reversedSeq1=Seq1[::-1]
print(reversedSeq1)

#028
dic={'A':'T', 'T':'A','G':'C','C':'G'}
for s in Seq1:
    print(dic[s],end='')
for s in Seq1:
    print(dic[s],end='')
for s in Seq1:
    print(dic[s],end='')
for s in Seq1:
    print(dic[s],end='')
print()

#029
if 'C' in Seq1:
    print("C 있음")
else : print("C 없음")

#030:
Seq1='AGTTTATAG'
for i in range(len(Seq1)):
    if Seq1[i:i+2]=='TT':
        print(f"TT 출현 index :{i}")

