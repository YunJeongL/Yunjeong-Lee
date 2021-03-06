# 반복문
# for => 지정된 횟수, 정해진 횟수
# while => 0 ~ 무한대
a = [1,2,3,4,5]
# 한 개씩 멤버를 제거하면서 출력하시오
# 조건식 : 언제까지? -> 멤버가 없을 때까지 -> while
# len(a)
while len(a)>0:
    print(a.pop())
#################################################
a = [1,2,3,4,5]
while a:
    print(a.pop())
#################################################
# 반복문이 정상적으로 다 돌아서 끝났음을 아는 방법
a = [1,2,3,4,5]
while a:
    print(a.pop())
else:
    print('정상적으로 다 루프를 돌았다')
#################################################
# 반복문이 정상적으로 다 돌아서 끝났음을 아는 방법
# 개수가 2개가 되면 종료
a = [1,2,3,4,5]
while a:
    print(a.pop())
    print('-----')
    if len(a) == 2:
        # 루프 중단
        break # while문을 빠져나간다(가장 가까운 반복문)
else:
    print('정상적으로 다 루프를 돌았다')
    
