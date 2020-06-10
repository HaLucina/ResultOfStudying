# coding: utf-8

#from pathlib import Path
import os
import Path
import glob
import re #pythonで正規表現を使うのに便利なの
import pprint #リストや辞書を整形して出 https://note.nkmk.me/python-pprint-pretty-print/


def old(filesPath):
    yield eto for eto in filesPath


p = Path(os.getcwd())
filesPath = sorted(p.glob("**/**"))


dirname, basename = os.path.split(old)
after =  basename[5:]
after =  basename[5:]
os.rename(old, os.path.join(dirname, after))
                
print('===END===')
input()


"""
- 超簡単書き換え https://gammasoft.jp/blog/text-file-edit-by-python/
- ↑と一緒に使いたい https://dev.classmethod.jp/articles/python-encoding/

- パクりたい https://qiita.com/takahori/items/fdf2f4e4586ea2bbc1aa





- 他の人の嫌いになったゲームブログ
    http://kuuyahiro.jugem.jp/?eid=127
    https://www.bodoge-intl.com/column/deai/

- ルール、用語がわからない
　（チートやあまりにもバランスがおかしいキャラやブキ以外で）
　　勝てないとかは努力が足りないだけ


- 結局ゲームが嫌いになる理由って"人"だよね
    

"""
