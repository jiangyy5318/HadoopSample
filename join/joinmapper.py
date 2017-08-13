#coding=utf-8
import os
import sys


filepath = os.environ["map_input_file"]
filename = os.path.split(filepath)[-1]
for line in sys.stdin:
    if line.strip() == "":
        continue
    fields = line[:-1].split("\t")
    sno = fields[0]
    if filename == 'data_info':
        name = fields[1]
        print '\t'.join((sno, '0', name))
    elif filename == 'data_grade':
        courseno = fields[1]
        grade = fields[2]
        print '\t'.join((sno, '1', courseno, grade))