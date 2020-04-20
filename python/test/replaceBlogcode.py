#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import glob
import re
import pprint
import os, sys
import fileinput


def convert_blogCard(args):
    url = re.search(r'\d+', args)
    syortCode = "{{< blogcard url=" + url + " >}}"
    return "blogCard"

def convert_tweet(args):
    num = re.search(r'\d+', args)
    syortCode = "{{< tweet " + num + " >}}"
    return "tweet"

def convert_imgUrl(args):
    jpg = re.search(r'', args)
    syortCode = "![test](/img/uploads/" + jpg + ")"
    return syortCode

def noMatch(args):
    return args


# https://qiita.com/hasegit/items/2cf05de74680717f9010
case = {
    ".*blogcard url.*"                          : convert_blogCard,
    ".*twitter.com/.*/status/.*"                : convert_tweet,
    ".*hackheatharu.xyz/wp-content/uploads/.*"  : convert_imgUrl,
    ".*" : noMatch
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

    #rewriteData = "\n".join(contents)
    [print(i) for i in contents]
    with open("result.md", mode="w", encoding="utf-8") as f:
        f.writelines(contents)

if __name__ == '__main__':  
    p   = Path(os.getcwd())
    mds = sorted(p.glob("**/*.md"))
    gen_iter = (os.path.abspath(f) for f in mds)    
    print(sys.getsizeof(gen_iter))

    for f in gen_iter:
        print(f)
        try: convert_code(f)
        except StopIteration: break


#input()
