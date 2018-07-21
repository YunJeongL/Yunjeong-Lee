# class 문법
# 사람이라는 유형의 객체를 파이썬으로 구현해보자 => 방법 : class
# 클래스의 이름은 첫글자 대문자 이어지는 글자 소문자 ~
# 클래스의 모든 함수의 첫번째 인자는 self 이다
# self는 자기 자신 class를 가르키는 키워드(예약어) <-> 타언어 : this
# 함수의 첫번째 인자는 self인데 실제 사용시에는 별도로 인자로 보지 않음(없다고 친다)
class Person:
    '''
    멤버 변수 : 객체의 속성
    '''
    name = None
    age = 0
    '''
    멤버 함수 : 객체의 행동(액션)
    '''
    def eat(self):
        print('eat() call')
    def sleeping(self):
        print('sleeping() call')
    '''
    생성자(constructor) 함수 : 객체(class의 인스턴스)를 생성하는 역할
                              메모리에 공간을 만들고 주소를 반환하는 역할
                              메모리에 공간을 만들고 주소 참조값 반환하고
                              참조 카운트 증가하는 역할
                              => 틀이 정해져 있다
    '''
    def __init__(self):
        print('생성자 call')

# 사용
# 클래스는 생성자를 호출하여 객체를 생성하는데 => 클래스명()
# 생성자() => 클래스명(인자값:생성자에서 정의한대로 배치)
obj = Person() 
# 멤버 변수나 멤버 함수를 사용하는 방법
# => 객체명.멤버변수, 객체명.멤버함수
print(obj.name, obj.age)
obj.sleeping()

# import random
# random.randint(0,1)