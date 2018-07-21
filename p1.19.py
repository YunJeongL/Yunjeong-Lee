# 모듈 가져와서 사용하기 및 만들기
# p1_mod.py를 가져와서 p1.19.py 본 코드에서 사용하겠다
# from 모듈명 import 모듈(클래스, 함수, 변수)

# 나는 XMan class를 가져다가 사용하고 싶다
from p1_mod import XMan
obj = XMan('멀티', 20)
print(obj.name)
obj.eat()