#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import glob
import re
import pprint
import os, sys
import fileinput


# https://qiita.com/hasegit/items/2cf05de74680717f9010
switch_case = (
    ("c.*", "Brooks Litchfield Conrad"),
    ("k.*", 'Michael Arthur Kinkade'),
    ("m.*", "Kevin Ford Mench")
)

# https://note.nkmk.me/python-str-replace-translate-re-sub/
# https://gist.github.com/ginrou/5787895
# https://gammasoft.jp/blog/text-file-edit-by-python/


def convert_code(file_name):
    with fileinput.FileInput(file_name, openhook=open(file_name,encoding  = "utf-8"), inplace=True, backup=".bak") as f:
        for line in f:
            replace_code = next(v for k,v in switch_case if re.match(k,line))  
            print("print = %s" % replace_code) 
            print(line.replace(line, replace_code), end="")

if __name__ == '__main__':  #このファイルを本体として実行した場合、mainが実行される。
    p   = Path(os.getcwd())
    mds = sorted(p.glob("**/*.md"))
    gen_iter = (os.path.abspath(f) for f in mds)    
    print(sys.getsizeof(gen_iter))

    for f in gen_iter:
        print(f)
        try: convert_code(f)
        except StopIteration: break


input()
