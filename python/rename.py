# coding: utf-8

from pathlib import Path
import glob
import re
import pprint
import os

tagetName   = '^(?=.*20xx).*$'
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
        print(result)
        #os.path.split(result)

print('===END===')
input()
