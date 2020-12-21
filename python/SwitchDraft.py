# coding: utf-8

from pathlib import Path
import glob
import fileinput
import pprint
import os

def listup_files(ETOS):
   yield[os.path.abspath(eto) for eto in ETOS]

def switchDraft(file_name):
    with fileinput.FileInput(file_name, inplace=True, backup=".bak") as f:
        [print(line.replace("draft: true", "draft: false"), end="") for line in f]
                 

if __name__ == '__main__': 
    print(os.path.dirname(os.path.abspath(__file__)))
    p = Path(os.path.dirname(os.path.abspath(__file__)))
    fList = sorted(p.glob("**/*.md"))
    pprint.pprint(['switch flase: ' + f.name for f in fList])
    [switchDraft(f.name) for f in fList]

print('===END===')
