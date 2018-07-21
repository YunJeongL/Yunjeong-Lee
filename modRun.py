# 모듈 사용
#from mod import PI, sum, A
#print(PI)

#(X)
#import mod.PI
#print(PI)

from a.b.mod import PI
print(PI)

# from a.b import mod
# print(mod.PI)

# 별칭 
from a.b import mod as m
print(m.PI)

import a.b.mod as m2
print(m2.PI)

print("="*20)
from a.b import *
print(mod.PI)

# python 3.x 자동지원
# 2.x 일 때는 a>b>__init__.py 안에
# __all__=['mod'] 내용을 기술해야 *이 적용된다

#################################
# a>b>__init__.py 모듈 가져오기
import a.b as bx
print(bx.sumEx(3,4))

import a.b as bx
print(bx.sumEx(5,6))

import a
print(a.NAME)

from a import NAME
print(NAME)

