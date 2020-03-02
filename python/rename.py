# coding: utf-8

from pathlib import Path
import glob
import re
import pprint

import os

tagetName   = "20xx年度報告書.xlsx"
after       = "2019年度報告書.xlsx"
p = Path(os.getcwd())

files = sorted(p.glob("**/*"))

for file_ in files:
    print(file_)

input()
