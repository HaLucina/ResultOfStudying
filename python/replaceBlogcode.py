#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys

def replace_func(fname, replace_set):
    target, replace = replace_set
    
    with open(fname, 'r') as f1:
        tmp_list =[]
        for row in f1:
            if row.find(target) != -1:
                tmp_list.append(replace)
            else:
                tmp_list.append(row)
    
    with open(fname, 'w') as f2:
        for i in range(len(tmp_list)):
            f2.write(tmp_list[i])

if __name__ == '__main__':  #このファイルを本体として実行した場合、mainが実行される。
    # param set
    fname = './test.txt'
    replace_setA = ('ccc =', 'ccc = 100\n') # (検索する文字列, 置換後の文字列)
    replace_setB = ('ddd =', 'ddd = N/A\n') # 最後の\nは改行コード
    
    # call func
    replace_func(fname, replace_setA)
    replace_func(fname, replace_setB)
