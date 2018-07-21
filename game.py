# 절차적 프로그래밍
# step0
# 아무것도 안넣으면 뭐라하고 다시 입력 받으세요
'''nameCheck = True
   while nameCheck:'''
while True:
    gameTitle = input("게임 제목을 입력하시오").strip()
    # 입력된 게임 제목의 길이가 28보다 크면 다시 입력
    if len(gameTitle) > 28:
        print('입력하신 "%s" 게임 제목은 최대 28자(현재 %s자 입력)를 초과할 수 없습니다. 다시 입력하세요...'
        % (gameTitle, len(gameTitle)))
    elif gameTitle == '':  # elif not gameTitle:
        print('아무것도 입력하지 않았습니다. 다시 입력하세요!\n')
    else:
        break

# step1 : 여러줄 문자열, 포맷팅, 치환식
introComment = '''
==============================
= {:^26} =
=           v1.0.0           =
==============================
'''.format(gameTitle)
print(introComment.strip())

# step2-2 : 게이머의 이름을 입력받는다
# 입력하지 않았을 경우에만 뭐라하고, 그 외에는 ok
while True:
    g_name = input('게이머의 이름을 입력하세요')
    # not => 부정한다 / 타언어 : !
    if not g_name:  # 이름을 입력안하면 "" => 조건식에서는 False => False 부정하면 True
                    # 이름을 입력하지 않았다고 판단
        print('이름이 입력되지 않았습니다. 다시~')
        continue   
    break

# step3 : 게임 방식 간단히 설명하고, 0 ~ 99까지 값을 입력하라고 코멘트 
# => 아무것도 안넣으면 뭐라하고, 0이하 99이상 넣어도 뭐라하고
game_rule = '''
본 게임은...
'''
print(game_rule)
while True:
    g_value = input("0 ~ 99 사이의 값으로만 AI의 값을 예측하여 입력하세요").strip()
    if not g_value: #공백을 입력하면
        print("값을 입력하세요")
        continue
    elif g_value.isalpha() and not g_value.isdecimal():
        print("숫자가 아닙니다")
        continue
    # else:
    #   print('ok')
    # 정수변환
    g_value = int(g_value)
    # 0보다 크고(0포함), 100보다 작고
    if g_value < 0 or g_value >= 100:
        print("값이 범위를 넘었습니다. 0~99 사이로 다시 입력")
        continue
    break
print(g_value,'ok')

# step4 : AI가 숫자 하나를 랜덤으로 생성한다 0 ~ 99
import random as r
comp_value = r.randint(0,99)

print('''
게임 이름  : %s
게이머 이름 : %s
내 입력값 : %s
AI 입력값 : %s
''' % (gameTitle, g_name, g_value, comp_value))

# step5 : AI의 숫자보다 유저가 입력한 숫자가 크거나 작으면 코멘트를 해준다
#         => 맞출 때까지 반복 
while True:
    import random as r
    comp_value = r.randint(0,99)
    if comp_value > g_value or comp_value < g_value:
        print('AI의 값과 입력한 값이 맞지 않습니다')
        continue
    elif comp_value == g_value:
        print('ok')
        break

# step6 :
'''  최종 숫자를 맞출 때까지 시도 횟수를 기록하여 최종 맞추면
     적절한 축하 코멘트 + 시도 횟수를 보여주고 + 
     100-시도횟수*10점을 보상으로 부여하여 보여준다
     -> 다시 게임할 것인지 물어보고 동의하면 다시 게임 시작 '''