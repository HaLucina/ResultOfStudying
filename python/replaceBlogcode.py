#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import glob
import re
import pprint
import os, sys
import fileinput

def listup_files(files):
    yield ([os.path.basename(f) for f in files])
    
#    convert_code(fname, replace_setA)
#    
#def convert_code(files):
#    with fileinput.FileInput(file_name, inplace=True, backup=".bak") as f:
#        for line in f:
#            print(line.replace("グーグルマップ", "Google マップ "), end="")

if __name__ == '__main__':  #このファイルを本体として実行した場合、mainが実行される。
    # param set
    p   = Path(os.getcwd())
    mds = sorted(p.glob("**/*.md"))
    gen_iter = (os.path.basename(f) for f in mds)
    print(sys.getsizeof(gen_iter))

    for f in gen_iter:
        print(f)
       # input()
