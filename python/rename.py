# coding: utf-8

from pathlib import Path
import glob
import re
import pprint
import os

inpStr = input(r"検索したい文字列を入力：")
after = input(r"置換したい文字列を入力：")

tagetName   = '^.*' + inpStr +'.*'
p = Path(os.getcwd())


absPaths = sorted(p.glob("**/**"))
repatter = re.compile(tagetName)


for path_ in absPaths:
    result = repatter.match(str(path_))
    if result == None: continue
    print(result.group())
    #無駄にif文を入れている理由→http://sookibizviz.blog81.fc2.com/blog-entry-1737.html
    
        
    else:
        #print(result.group())
        dirname, basename = os.path.split(result.group())
        print('dir = ' + dirname)
        os.rename(result.group(), os.path.join(dirname, after))
                
print('===END===')
input()
