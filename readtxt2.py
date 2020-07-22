#! /usr/bin/env python

import sys
import json

def read_txt(file_name:str) -> str :
    ret=''
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith('>') :
                continue
            ret+=line.strip()
        return ret

def read_csv(file_name:str) -> list:
    ret =list()
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header=line.strip().split(",")
                continue
            splitted = line.strip.sprit(",")
            d=dict(zip(header,splitted))
            ret.append(d)
    return ret

def read_tsv(file_name:str) -> list:
    ret=[]
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith('#') :
                header=line.strip().split('\t')
                continue
            splitted = line.strip().split('\t')
            d=dict(zip(header, splitted))
            ret.append(d)
    return ret

def write_json(l: list,fimename:str) -> None:
    with open(filename, 'w') as handle:
        json.dump(l, handle, indent=4)

def read_json(file_name:str) -> list:
    with open(file_name, 'r') as handle:
        l=json.load(handle)
        return l




