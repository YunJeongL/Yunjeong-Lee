# 예외 처리
# 프로그램은 안정적으로 작동해야 하고, 죽으면 안된다!
# 내가 작성한 코드를 try로 감싸서 잘못 입력된 부분에 대해 죽지않고
# 정상적으로 다시 작동할 수 있게 처리해준다

try:
    print(1)
    print(1/0)
    print(2)
except Exception as e: # 오류를 잡는 부분(오류 있으면 수행)
    print(3,e)
else:  # 오류 없으면 수행
    print(4)
finally:  # 무조건 수행됨
    print(5)
