# 절차적 프로그래밍
while True:
    gameTitle = input("게임 제목을 입력하시오").strip()
    if len(gameTitle) > 28:
        print('''입력하신 "%s" 게임 제목은 최대 28자(현재 %s자 입력)를 초과할수 없습니다. 다시 입력하세요.. ''' % (gameTitle, len(gameTitle)) )
    elif len(gameTitle)==0:
        print('아무것도 입력하지 않았습니다. 다시!!\n')
    else:
        break
# step 1-1 : 여러줄 문자열, 포멧팅, 치환식
introComment = '''
==============================
= {0:^26} =
=           v1.0.0           =
==============================
'''.format(gameTitle)
print( introComment.strip() )
# step 2-2 : 게이머의 이름을 입력받는다?
nameCheck = True
while nameCheck:
    g_name = input('게이머의 이름을 입력하세요?').strip()
    if not g_name: 
        print('이름이 입력되지 않았습니다. 다시~')
        continue
    nameCheck = False
# step 3 : 게임 방식 간단히 설명하고, 0 ~ 99까지 값을 입력하라고 코멘트 -> 아무것도 안넣으면 뭐라하고, 0이하 99이상 넣어도 뭐라하고
game_rule = ''' 본 게임은 ... '''
print(game_rule)

comp_value = None
tryCount = 0
# 본 게임 구성부분
while True:
    # step 4-1 : 사용자로부터 수치값을 입력받는다
    while True:
        g_value = input('0 ~ 99사이의 값으로만 AI의 값을 예측하여 입력하세요').strip()
        if not g_value: # 공백을 넣으면
            print('값을 정확하게 입력하세요')
            continue
        elif g_value.isalpha() and not g_value.isdecimal():
            print('숫자가 아닙니다')
            continue
        g_value = int(g_value)
        if  0 > g_value or g_value >= 100:
            print('값이 범위를 넘었습니다. 0~99 사이로 다시 입력')
            continue
        break

    # step 4-2 : AI가 숫자 하나를 랜덤으로 생성한다 0 ~ 99
    import random as r
    # False 상태인 경우만 체크하고 싶으면 해당 조건식을 부정
    if not comp_value: 
        comp_value = r.randint(0, 99)

    print('''
    게임 이름  : %s
    게이머 이름 : %s
    내 입력값 : %s
    AI 입력값 : %s
    ''' % (gameTitle, g_name, g_value, comp_value))
    
    # step 5 : AI의 숫자보다 유저가 입력한 숫자가 크거나 작으면 코멘트를 해준다 => 맞출때까지 반복
    # if g_value == 0:break  # 임시
    # 시도 횟수 증가
    tryCount += 1
    if g_value > comp_value:
        print('AI값보다 큽니다')
    elif g_value < comp_value:
        print('AI값보다 작습니다')
    else: #정답
        print('''
        정답입니다. 게이머 : {0}, AI : {1}
        {name}님의 총 시도횟수는 {count}입니다.
        획득 점수는 {point}입니다.'''.format(g_value, comp_value, name=g_name, count=tryCount, point=100-tryCount*10))
        break

'''
step 6 : 
-> 최종 숫자를 맞출때까지 시도 횟수를 기록하여 최종 맞추면
-> 적절한 축하 코멘트 + 시도 회수를 보여주고 + 
    100-시도회수*10점을 보상으로 부여하여 보여준다
-> 다시 게임할것인지 물어보고 동의하면 다시 게임 시작
'''