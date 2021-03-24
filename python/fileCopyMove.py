# coding: utf-8
import sys
from pathlib import Path
import glob
import re #pythonで正規表現を使うのに便利なの
import pprint #リストや辞書を整形して出 https://note.nkmk.me/python-pprint-pretty-print/
#import xlwings as xw
import os
import shutil


#xw.App().screen_updating = false
#wb = xw.Book()
#wb.save(r'D:\☆彡書類作成環境\my_lib\new_file.xlsx')
#xw.App().kill(r'D:\☆彡書類作成環境\my_lib\new_file.xlsx')
#xw.App().screen_updating = true



if __name__ == '__main__':
    pwd = Path.cwd()
    dirs = sorted(pwd.glob('*'))
    tage = 'new_file.xlsx'

    #shutil.move()が上手くいかない。以下のエラーが出る。
    #AttributeError: 'WindowsPath' object has no attribute 'rstrip'
    #原因：バグ。解決策は移動先のdirパス指定にfile名まで記載しなければならない。
    #参考 https://tec.citrussin.com/entry/2019/03/24/201649
    d = pwd.joinpath('ほげ/old/new_file.xlsx')
    f = pwd.joinpath('ほげ/new_file.xlsx')
    shutil.move(f, d)
    #参考 https://excel-ubara.com/python/python020.html
   # for p in dirs:
   #     if p.is_dir():
   #         #p.joinpath('old').mkdir()
   #         filesInP = p.glob('**/*.*')
   #         d = p.joinpath('old')
   #         print([shutil.move(f, d) for f in filesInP])
    #pprint.pprint([p.joinpath('old').mkdir() for x in outputContents(p)])
    # [shutil.copy(tage, x) for x in outputContents(p) if not x == p]
