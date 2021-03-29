# coding: utf-8
import sys
sys.path.append('../')
import target
import settings

def hoge():
	print(settings.CONST_VALUE)
	target.tageHoge()

if __name__ == "__main__":
	print('calld test1 hoge')
	hoge()
