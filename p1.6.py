# 파이썬 기초 순서
'''
2. 연속 데이터 관련 / 시퀀스 타입
- 튜플 : (), 순서 있다, 값의 중복 관계 없음, 값을 묶는다
  tuple : 튜플의 멤버가 1개일 경우 (1,)
  함수 내부에서 여러 개의 값이 리턴될 때 많이 활용
'''
print('='*70)

tu = ()
print(tu, len(tu), type(tu))
a = (1)
print(a, type(a))
a = (1,)
print(a, type(a))
# 값의 변화 불가, 삭제 불가, 변경 불가 => immutable
# 단순히 값을 묶는데 본질이 있음
tu = (1,2,3,4)
print(tu[0])
print(tu[:2])
a=(5,6,7,8)
# 튜플이나 리스트의 합은 그냥 2개가 이어져서 하나의 튜플, 리스트가 된다
print(tu + a)