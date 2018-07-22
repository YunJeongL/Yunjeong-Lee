# 문자열의 정체 체크
a = 'b'
print(a.isalpha(), a.isdecimal(), a.isdigit(), a.isalnum())
a = '1'
print(a.isalpha(), a.isdecimal(), a.isdigit(), a.isalnum())
a = '가'
print(a.isalpha(), a.isdecimal(), a.isdigit(), a.isalnum())
a = '1.1'
print(a.isalpha(), a.isdecimal(), a.isdigit(), a.isalnum())
# 정수 => isalpha():F and isdecimal():T

#####################################################################
# 랜덤
# as 별칭
# import 모듈 가져오기 표현
import random as r
for n in range(100):
    # randint() -> x <= r <= y
    print(r.randint(0,2))
