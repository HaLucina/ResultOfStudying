# coding: utf-8
import target
from test import settings

def hoge():
	print(settings.CONST_VALUE)
	target.tageHoge()

if __name__ == "__main__":
	print('calld test2 hoge')
	hoge()
