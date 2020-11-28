# coding: utf-8

from pathlib import Path
import glob
import fileinput
import pprint
import os
import shutil

file_name = "example.txt"
back_name = file_name + ".bak"
shutil.copy(file_name, back_name)
data = []


if __name__ == '__main__': 
    print('===START===')

    with open(file_name, 'r') as f:
        data = f.readlines()
        data.sort()
        [print(line.rstrip()) for line in data]

    with open(file_name, 'w') as f:
        f.write("".join(data))
        
    print('===END===')
