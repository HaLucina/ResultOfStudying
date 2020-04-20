#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import glob
import re
import pprint
import os, sys
import fileinput

def notMatch(args):
    return args

def convert_card(args):
    return "hoge"

# https://qiita.com/hasegit/items/2cf05de74680717f9010
case = {
    ".*blogcard.*" : convert_card,
    "k.*": 'Michael Arthur Kinkade',
    "m.*": "Kevin Ford Mench",
    ".*": notMatch
}

# https://note.nkmk.me/python-str-replace-translate-re-sub/
# https://gist.github.com/ginrou/5787895
# https://gammasoft.jp/blog/text-file-edit-by-python/


def convert_code(file_name):
    contents = []
    with open(file_name, encoding="utf-8") as f:
        #replace_code = next(v for k,v in switch_case if re.match(k,line))  
        for line in f.readlines():
            replace_methoed = next(case[k] for k in case if re.match(k, line))
            contents.append(replace_methoed(line))

    [print(i) for i in contents]
    with open(file_name, mode="w", encoding="utf-8") as f:
        f.write(contents)

if __name__ == '__main__':  #このファイルを本体として実行した場合、mainが実行される。
    p   = Path(os.getcwd())
    mds = sorted(p.glob("**/*.md"))
    gen_iter = (os.path.abspath(f) for f in mds)    
    print(sys.getsizeof(gen_iter))

    for f in gen_iter:
        print(f)
        try: convert_code(f)
        except StopIteration: break


#input()
