#coding=utf-8
import sys


lastsno = ""

for line in sys.stdin:
    if line.strip() == "":
        continue
    fields = line[:-1].split("\t")
    sno = fields[0]
    if sno != lastsno:
        name = ""
        if fields[1] == "0":
            name = fields[2]
    elif sno == lastsno:
        if fields[2] == "1":
            courseno = fields[2]
            grade = fields[3]
            if name:
                print '\t'.join((lastsno, name, courseno, grade))
    lastsno = sno