# 절차적 + 함수지향적 프로그래밍
import random
 
def log(msg):
    isTest = True
    if isTest:
        print('-'*20)
        print(msg)
        print('-'*20)

def inputAndtrim(promptStr='입력하세요'):
    return input(promptStr).strip()

def lyj_gameStart():
    while True:
        # gameTitle은 함수 안에서만 의미를 가지는 지역변수
        gameTitle = inputAndtrim("게임 제목을 입력하시오")
        if len(gameTitle) > 28:
            log('''입력하신 "%s" 게임 제목은 최대 28자(현재 %s자 입력)를 초과할수 없습니다. 다시 입력하세요.. ''' % (gameTitle, len(gameTitle)) )
        elif not gameTitle:# 미입력하면, len(gameTitle)==0:
            log('아무것도 입력하지 않았습니다. 다시!!\n')
        else:
            break
    return gameTitle

def lyj_gameTitleDisplay(gameTitle, icon):
    # step 1-1 : 여러줄 문자열, 포멧팅, 치환식
    introComment = '''
==============================
= {0:^26} =
=           v1.0.0           =
==============================
'''.format(gameTitle)
    # replace() 문자열 멤버 함수로 특정 문자열을 대체
    print( introComment.strip().replace('=',icon))

def lyj_gameInputPlayerName(prompt):
    # step 2-2 : 게이머의 이름을 입력받는다
    nameCheck = True
    while nameCheck:
        g_name = inputAndtrim(prompt)
        if not g_name: 
            print('이름이 입력되지 않았습니다. 다시~')
            continue
        nameCheck = False
    return g_name

def lyj_gameIntro():
    # step 3 : 게임 방식 간단히 설명하고, 0 ~ 99까지 값을 입력하라고 코멘트 -> 아무것도 않넣으면 모라하고, 0이하 99이상 넣어도 모라하고
    game_rule = ''' 본 게임은 ... '''
    print( game_rule )

def lyj_gameInit():
    # 게임 변수 초기화
    comp_value = None
    tryCount = 0
    return comp_value, tryCount

def lyj_gamePlaying(g_name1,comp_value1,tryCount1):
    g_name = g_name1
    comp_value = comp_value1
    tryCount = tryCount1
    # 본 게임 진행 
    while True:
        # 사용자로부터 수치값을 입력받는다
        while True:
            g_value = inputAndtrim('0 ~ 99사이의 값으로만 AI의 값을 예측하여 입력하세요')
            if not g_value:# 공백을 넣으면
                print('값을 정확하기 입력하세요')
                continue
            elif g_value.isalpha() and not g_value.isdecimal():
                print('숫자가 아닙니다')
                continue
            g_value = int(g_value)
            if  0 > g_value or g_value >= 100:
                print('값이 범위를 넘어었습니다. 0~99 사이로 다시 입력')
                continue
            break
    
def lyj_gameAgain():
    # 다시할것인가?
    while True:
        res = input('다시 게임을 할까요?(yes/no)').strip().upper()
        # yes : Yes, YES, yES => 대문자로만 혹은 소문자로만 체크
        if res == 'YES':
            # 86라인 반복문 빠져나가기
            break
        # no
        elif res == 'NO':
            # 전체 게임 빠져나가기 30라인
            isGamePlaying = False
            # 86라인 반복문 빠져나가기
            break
        # 이도 저도 아닐때
        else:
            print('정확하게 (yes/no)로 입력하세요')



def lyj_gameEnd():
    print('game over !! bye bye~')




def start():
    # 프로그램 시작
    log('함수 중심으로 구성된 게임 시작')
    # 게임제목 처리 함수
    g_title = lyj_gameStart()
    icons = ['☆','★','◎','♠']
    idx = random.randint(0,3)
    lyj_gameTitleDisplay(g_title,icons[idx])
    # 게임플레이어 이름 획득
    g_name = lyj_gameInputPlayerName('게이머의 이름을 입력>>')
####################################################################
    lyj_gameIntro()
    isGamePlaying = True
    while isGamePlaying:
        # 멤버 2개짜리 튜플을 리턴하니까 변수 2개로 받는다(의미부여)
        comp_value, tryCount = lyj_gameInit()
        lyj_gamePlaying(g_name,comp_value,tryCount)
        isGamePlaying = lyj_gameAgain()

        lyj_gameEnd()
####################################################################
# 게임실행
start()

