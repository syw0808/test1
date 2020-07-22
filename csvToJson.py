#! /usr/bin/env python
import sys 
import readtxt

if len(sys.argv)!=2 :
    print(f"#usage : python {sys.argv[0]} [csv]")
    sys.exit()

f=sys.argv[1]

"""
l=readtxt.read_tsv(f)
readtxt.to_json(l,"read_sample2.json")
"""
l=readtxt.read_csv(f)
readtxt.to_json(l, "read_sample3.json")

readtxt.read_json("read_sample3.json")

