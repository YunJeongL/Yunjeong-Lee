class Person2:
   
    name = None
    age = 0
    
    def eat(self):
        print('eat() call')
    def sleeping(self):
        print('sleeping() call')
    # 생성자의 주업무 중 하나는 멤버변수 초기화에 있다
    def __init__(self, name, age):
        # 클래스 내부에서 멤버들을 사용할 경우 무조건 self. 붙인다
        self.name = name
        self.age = age
        print('생성자 call')

p1 = Person2('장영환', 25)
p2 = Person2('한준모', 25)

# 이름을 출력하시오
print(p1.name)
print(p2.name)
#################################################################
# XMan 정의한다
# XMan은 Person2를 상속받는다 => XMan은 Person2이다 : is a
# Person2는 XMan이다(X) : 
# Person2는 XMan을 자식으로 가진다 : has a
# dog은 동물이다 : is a 
# 동물은 dog이다(X) => 동물은 dog를 자식으로 가진다 : has a
#################################################################
# class 클래스명(부모): => 상속을 표현
# 부모가 Object인 경우 생략 가능
# class Person2(Object) or class Person2
# 상속을 받으면 부모의 모든 것을 다 사용할 수 있다
# 자식을 별도로 변수, 함수를 추가할 수 있다
# 자식은 물려받은 부모의 것을 재정의(업그레이드)할 수 있다
class XMan(Person2):
    abil = 100
    def speed(self):
        print('시속 200km로 달린다')
    # 부모로부터 받은 함수를 재정의하여 사용
    def eat(self):
        print('밥을 1초만에 다 먹을 수 있다')
    def __init__(self, name, age):
        self.name = name
        self.age = age

xman = XMan('장영환2', 25)
print(xman.name, xman.abil) 