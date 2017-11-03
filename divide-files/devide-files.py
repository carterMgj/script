#!/usr/bin/env python
# encoding: utf-8

import os
import shutil
import sys

file_list = []

def list(rootDir):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        file_list.append(path)
        if os.path.isdir(path):
            list(path)

if __name__ == '__main__':
    list(os.getcwd())
    f = 0
    if len(sys.argv) == 1:
        print 'please input a number!'
        exit()
    else:
        index = int(sys.argv[1])
    for i in file_list:
        if file_list.index(i) % index == 0:
            dirname = str(f)
            f += 1
            os.makedirs(dirname)
            shutil.move(i, dirname)
        else:
            shutil.move(i, dirname)

