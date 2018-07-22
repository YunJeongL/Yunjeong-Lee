# 참조 카운트 : 객체 속성
import sys
a = 1
print(a, type(a), sys.getrefcount(1))
b = 1
print(b, type(b), sys.getrefcount(1))
print(a is b)
del(a)  # 참조를 끊는 것
print(sys.getrefcount(1))
#print(a is b)
# 파이썬에 존재하는 모든 요소는 객체다
# 파이썬에서 사용하는 것들 중에 예를 들어 1,2,3, 이런 것들도 객체고
# 단지 참조를 통해서 해당 객체를 사용할 뿐이다
from a.b.mod import A
obj = A()
print('객체A : ', sys.getrefcount(A))

del(obj)
print('객체A : ', sys.getrefcount(A))
obj2 = A()
print('객체A : ', sys.getrefcount(A))