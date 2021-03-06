# 파이썬 기초 순서
'''
2. 연속 데이터 관련 / 시퀀스 타입

- 리스트 : [], 순서(인덱스:0~, ~-1)가 있다, 값의 중복허용
- 딕셔너리 : {}, 순서가 없다, 키와 값의 세트로 멤버 구성, 키는 고유하고 값은 중복되도 상관없음
- 튜플 : (), 순서 있다, 값의 중복 관계 없음, 값을 묶는다
- 집합 : set(), 중복제거, 순서는 중요하지 않음
'''
print('='*70)
nums = None #타입이 없다, 값이 없다
# 비어있는 리스트 객체를 생성해서 반환, 비어있는 리스트 생성
nums = []
print(nums, len(nums), type(nums))
nums = list()
print(nums, len(nums), type(nums))
# 0보다 크고 10보다 작은 정수들 중에 홀수만 멤버인 리스트 생성
nums = [1,3,5,7,9]
print(nums, len(nums), type(nums))
anis = ['dog','cat','bird']
print(anis, len(anis), type(anis))
# 리스트의 멤버들의 타입이 동일할 필요없다
mix = [1,2,3,'dog','cat']
print(mix, len(mix), type(mix))
# 차원을 뒤섞으면?
multiMetrix = [1,2,3,['dog',10]]
print(multiMetrix, len(multiMetrix), type(multiMetrix))
#============================================================================
# mix라는 리스트에서 3을 출력하시오 => 인덱싱 => 리스트의 인덱싱
print(mix[2])
# multiMatrix 리스트에서 dog을 출력하시오
print(multiMetrix[3][0])
# 슬라이싱
nums = [1,3,5,7,9]
# nums 리스트에서 3,5,7만 멤버로 가진 리스트를 구하시오
print('사본작업', nums[1:-1])
print(nums) # 원본은 변경되지 않음(인덱싱,슬라이싱)
# 특정 멤버 변경
nums[0] = 100
print(nums)
# 3,5,7을 전부 -1로 변경하시오
# 슬라이싱된 리스트에 값을 대입할 경우에는 하나의 값이 아닌 연속값 형태로 대입해야 교체가 된다
nums[1:-1]='he'
print(nums)
###########################################################################
# 리스트 삭제
nums = [1,3,5,7,9]
print(nums)
# 0번 인덱스 멤버 제거
del nums[0]
print(nums)
# 처음부터 1번 인덱스까지 멤버 제거
del nums[:2]
print(nums)
# 7이란 값을 가진 멤버 제거
nums.remove(7)
print(nums)
# 다 제거
nums.clear()
print(nums)
##################################################
# 추가, 정렬
nums.append(100)
print(nums)
nums = [4,2,3,5,6,4,34,65,47,234,1]
# 정렬 
nums.sort()
print(nums) 
# 원본은 훼손하지 않고 오른차순 정렬하여 3번째 값을 출력하시오
nums = [4,2,3,5,6,4,34,65,47,234,1]
# 사본 획득
nums2=nums[:]
# 정렬
nums2.sort()
# 데이터 출력
print(nums[2])
print('원본확인', nums)
################################################################3
# 연속 데이터(컬렉션, 시퀀스 데이터) 여러개 데이터를 하나의 이름(변수명)으로 관리하고,
# 프로그램을 좀 더 편하게 구성하기 위해서 나온 방식