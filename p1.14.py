# 함수 : function <-> 메쏘드(method)
# 왜 : 반복작업 해소 -> 생산성이 높아짐, 개발속도 향상, 재사용성 높아짐 (함수의 장점)

a = 1
b = 2
c = a + b
print(c)
# 5+6, 7+8, 10+12,...
# [..] => 생략가능하다
# def 함수명([인자이름,...]):
#     함수 내부에서 할 일 기술
#     [return 결과값]
def sum(x,y):
    return x + y
# 함수 호출 => 함수명()
d = sum(a,b)
print(d)

# 가변 인자(arguments or params)
def sum2(*args):
    # 전달된 인자가 모두 정수값이라면
    # 인자의 총합을 구해서 리턴하시오
    print(type(args))
    sum = 0
    for n in args:
        sum += n  # sum = sum + n
    return sum

print('누적합 결과 -> ', sum2(1,2))
print('누적합 결과 -> ', sum2(1,2,3))
print('누적합 결과 -> ', sum2(1,2,3,4))
print('누적합 결과 -> ', sum2(1,2,3,4,5))
print('누적합 결과 -> ', sum2(1,2,3,4,5,6))

# 주어진 리스트의 모든 멤버의 누적곱을 구하시오
data = [1,2,3,4]
def mul(input):
    # 중간 중간 계산값을 담고 있을 변수
    tmp = 1
    for n in input:
        tmp *= n
        print(tmp)
    return tmp
print('누적곱 : ', mul(data))

# 주어진 리스트의 모든 멤버의 누적합, 누적곱을 구해서 리턴하시오
# -> 함수의 리턴값이 2개다

def mix(list):
    s = 0  # 누적합의 임시 데이터를 담는 변수
    m = 1  # 누적곱의 임시 데이터를 담는 변수
    for n in list:
        s += n
        m *= n
    return s, m

print(mix(data)) # 결과의 타입이 튜플(값을 묶는다)

t_sum, t_mul = mix(data)
print('t_sum = %s, t_mul = %s' %(t_sum, t_mul))
######################################################################
def mixEx(list):
    s = 0  # 누적합의 임시 데이터를 담는 변수
    m = 1  # 누적곱의 임시 데이터를 담는 변수
    for n in list:
        s += n
        m *= n
    return {'t_sum':s, 't_mul':m}
nRtn = mixEx(data)
print('합',nRtn['t_sum'])
print('곱',nRtn['t_mul'])
######################################################################
# 문자열을 입력받아서 앞뒤 공백을 제거하고 리턴해주는 함수를 만드시오
######################################################################
# 정의
def rem(str):
    str = input('문자열을 입력하세요')
    ss=str.strip()
    return ss

# 테스트
print(rem(str)) 
######################################################################
# 정의
def trim(str):
    return str.strip()

# 테스트
print(trim('            하이            '))
######################################################################
# 카테고리
# 사용자 정의 함수 : trim()
# 내장 함수 : type(), len()
# 멤버 함수 : random.randint()
######################################################################
isTest = True  # False
def log(msg):
    if isTest:
        print('-'*20)
        print(msg)
        print('-'*20)

log('helloworld')
#################################################################
# 함수 인자에 초기값 부여하여 활용
def setPerson(name, age, weight=80):
    log('이름 = %s 나이 = %s 무게 = %s' %(name, age, weight))

setPerson('홍길동', 100, 70)
setPerson('홍길동2',100) #무게를 입력안하면 기본값 80으로 나옴

# setPerson() -> 이름 나이 무게의 기본값이 지정되어있는 경우 사용가능
def setPerson2(name='멀티', age=50, weight=80):
    log('이름 = %s 나이 = %s 무게 = %s' %(name, age, weight))
setPerson2()
setPerson2('역삼')
setPerson2(weight=100)

a = [15,20,3]
a.sort() # 기본값 reverse=False
print(a)
a.sort(reverse=True)
print(a)
