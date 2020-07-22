#! /usr/bin/env python

l =['A','C','G','T']
"""
st=''
for i in l:
    st+=i
    for j in l:
        st+=j
        for k in l:
            st+=k
            print(st)
            st=st[:2]
        st=st[0]
    st=''
"""

def mer(l1, l2, n):
    ltmp=[]
    if n==1 : 
        return l2

    for s1 in l1:
        for s2 in l2 :
            ltmp.append(s1+s2)

    return mer(l1,ltmp,n-1)

mers = mer(l,l,3)
print(mers)
