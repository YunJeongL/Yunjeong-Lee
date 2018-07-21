# 파이썬 기초 순서
'''
2. 연속 데이터 관련 / 시퀀스 타입
- 집합 : set(), 중복제거, 순서는 중요하지 않음
'''
print('='*70)

a = 'helloworld'
# a가 가리키는 문자열의 중복 문자 제거
b = set(a)
print(b)
c = list(b)
print(c)
c.sort()
print(c)
# 원본데이터 => set() 중복제거 => 특정 시퀀스타입 변화 => 원하는 업무 진행
###############################################################################
# 합집합, 교집합, 차집합
a = set([1,3,5,7,9,2,6,5])
b = set([2,4,6,8,1,5,4])
print(a,b)
# 합집합
print(a.union(b))
# 교집합
print(a.intersection(b))
# 차집합 : 방향에 따라 결과 다름 a-b, b-a
print(a.difference(b))
print(b.difference(a))