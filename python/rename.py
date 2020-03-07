# coding: utf-8

from pathlib import Path
import glob
import re
import pprint
import os

inpStr = input(r"任意の文字列を入力：")

tagetName   = '^.*' + inpStr +'.*'
after       = r"2019年度報告書.xlsx"
p = Path(os.getcwd())


files = sorted(p.glob("**/*.xls*"))
repatter = re.compile(tagetName)


for file_ in files:
    result = repatter.match(str(file_))

    #無駄にif文を入れている理由→http://sookibizviz.blog81.fc2.com/blog-entry-1737.html
    if result == None:
        continue
    else:
        #print(result.group())
        dirname, basename = os.path.split(result.group())
        print('dir = ' + dirname)
        os.rename(result.group(), os.path.join(dirname, after))
                
print('===END===')
input()
