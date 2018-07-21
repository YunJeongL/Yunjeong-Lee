# 파이썬 기초 순서
'''
4. 게임 제작
  -> 게임을 만들어가면서 조건문, 반복문, 식(비교식,..) 확인
  -> 0 ~ 99까지의 숫자를 맞추는 게임
  -> step0 : "게임의 이름을 입력하시오" 코멘트가 나오고
  "Enjoy number matching game" 입력하면 아래처럼 출력
  -> step1 : 게임이 시작하면 코멘트 안내하고 입력 유도
  ==============================
  = 게임 제목이 입력됨(중앙정렬) =
  =           v1.0.0           =
  ==============================
  게이머의 이름을 입력하세요 
  
  -> 유저는 게임을 시작할 때 이름을 넣고 플레이를 시작하며 
     숫자를 입력하여 맞추기를 시작한다
     숫자를 잘못 넣으면 뭐라하고 다시 입력 유도
  -> 게임이 시작하면 AI가 숫자를 하나 생성한다
  -> AI의 숫자보다 유저가 입력한 숫자가 크거나 작으면 코멘트를 해줌
     최종 숫자를 맞출 때까지 시도 횟수를 기록하여 최종 맞추면
     적절한 축하 코멘트 + 시도 횟수를 보여주고 + 
     100-시도횟수*10점을 보상으로 부여하여 보여준다
  -> 다시 게임할 것인지 물어보고 동의하면 다시 게임 시작
'''

# 콘솔에서 사용자의 입력을 대기하다가 사용자 입력 후 엔터치면 반환
a = input('게이머의 이름을 입력하세요')
print('사용자의 입력값 : ', a)