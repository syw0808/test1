#! /usr/bin/env python


with open("read_sample.txt","r") as handle :
    for line in handle :
        print(line.strip())
