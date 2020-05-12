#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import glob
import re
import pprint
import os, sys
import fileinput

#https://note.nkmk.me/python-str-extract/

def convert_draft(args):
    print("hoge")
    return "thumbnailImage: https://res.cloudinary.com/ddghc4l09/thumbnail/spl2.jpg\ndraft: true\n"        


def convert_blogCard(args):
    try:
        url = re.findall(r'"(.*)"', args)
        syortCode = "{{< blogcard url=" + url[0] + " >}}"
        return syortCode
    except:
        return args        

def convert_tweet(args):
    try:
        num = re.findall(r'status/(.*)', args)
        syortCode = "{{< tweet " + num[0] + " >}}"
        return syortCode
    except:
        return args        

def convert_imgUrl(args):
    try:
        jpg = re.findall(r'uploads/(.*)"><img', args)
        syortCode = "![test](/img/" + jpg[0] + ")"
        return syortCode
    except:
        return args        

def noMatch(args):
    return args


# https://qiita.com/hasegit/items/2cf05de74680717f9010
case = {
         ".*thumbnailImage:.*"                              : convert_draft,
    # "![test].*"                              : convert_draft,
    #".*blogcard url.*"                          : convert_blogCard,
    #".*twitter.com/.*/status/.*"                : convert_tweet,
    #".*hackheatharu.xyz/wp-content/uploads/.*"  : convert_imgUrl,
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
    #[print(i) for i in contents]
    with open(file_name, mode="w", encoding="utf-8") as f:
        f.writelines(contents)

if __name__ == '__main__':  
    p   = Path(os.getcwd())
    mds = sorted(p.glob("**/*.md"))
    gen_iter = (os.path.abspath(f) for f in mds)    

    for f in gen_iter:
        print(f)
        try: convert_code(f)
        except StopIteration: break


input()
