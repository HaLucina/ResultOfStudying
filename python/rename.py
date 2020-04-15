# coding: utf-8

#from pathlib import Path
import os
import Path
import glob
import re #pythonで正規表現を使うのに便利なの
import pprint #リストや辞書を整形して出 https://note.nkmk.me/python-pprint-pretty-print/

inpStr = input(r"検索したい文字列を入力：")
after = input(r"置換したい文字列を入力：")

tagetName   = '^.*' + inpStr +'.*'
p = Path(os.getcwd())
filesPath = sorted(p.glob("**/**"))
repatter = re.compile(tagetName) #https://docs.python.org/ja/3/howto/regex.html#compiling-regular-expressions

for path_ in absPaths:
    result = repatter.match(str(path_))
    if result == None: continue
    print(result.group())
    #無駄にif文を入れている理由→http://sookibizviz.blog81.fc2.com/blog-entry-1737.html
  
# どうしてもリスト型で欲しいならジェネレート関数で作成するとメモリ消費を抑えられる
# def listup_files(ETOS):
#   yield[eto for eto in ETOS]
        
#else:
#        #print(result.group())
#        dirname, basename = os.path.split(result.group())
#        print('dir = ' + dirname)
#        os.rename(result.group(), os.path.join(dirname, after))
                
print('===END===')
input()
