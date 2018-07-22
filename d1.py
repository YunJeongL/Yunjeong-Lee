'''
파이썬에서 maria db를 접속하고, 쿼리 수행
1. 접속, 해제
'''
import pymysql as my

try:
# 디비 오픈
    conn = my.connect(host='127.0.0.1',
                        #port = '3307'(포트가 다른 사람은 변경),
                        user='root',
                        password='1419',
                        db='pythondb',
                        charset='utf8')
    print('연결성공')
    # 디비 닫기
    conn.close()
    print('닫기성공')

except Exception as e:
    print(e)