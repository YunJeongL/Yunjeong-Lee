# 반복문 (while, for)
a = [1,2,3,4,5]
# 리스트 a의 멤버들을 하나씩 꺼내서 출력하시오
# for each 방식만 지원
for item in a:
    print(item)

a = [(1,2),(3,4),(5,6)]
for i in a:
    print(i)
for i,j in a:
    print(i,j)
for i in a:
    print(i[0],i[1])

# 연속수 -> range(x,y)
# x <- n < y
for n in range(1,11):
    print(n)
'''
3단~7단까지 출력하시오 => 이중 for문
3 x 1 = 3
3 x 2 = 6
...
7 x 9 = 63
'''
# 3 ~ 7 : range(3,8)
# 1 ~ 9 : range(1,10)
for i in range(3,8):
    for j in range(1,10):
        print('%s x %s = %2s' %(i, j, i*j))

for i in range(3,8):
    for n in range(1,10):
        print(i*n)

# 축약 
# 똑같은 결과를 바로 리스트에 담기
print(['%s x %s = %2s' %(i, j, i*j) for i in range(3,8) for j in range(1,10)])        