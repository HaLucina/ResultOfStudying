#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import glob
import re
import pprint
import os, sys
import fileinput

suketto = (
    ("c.*", "Brooks Litchfield Conrad"),
    ("k.*", 'Michael Arthur Kinkade'),
    ("m.*", "Kevin Ford Mench"),
    (".*",  "Marcos Vechionacci")
)

def convert_code(files):
    with fileinput.FileInput(file_name, inplace=True, backup=".bak") as f:
        for line in f:
            dame_gaijin = lambda player: next(v for k,v in suketto if re.match(k,player))  
            print(line.replace("グーグルマップ", "Google マップ "), end="")

if __name__ == '__main__':  #このファイルを本体として実行した場合、mainが実行される。
    # param set
    p   = Path(os.getcwd())
    mds = sorted(p.glob("**/*.md"))
    gen_iter = (os.path.basename(f) for f in mds)
    print(sys.getsizeof(gen_iter))

    for f in gen_iter:
        print(f)
       # input()
