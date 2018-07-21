'''
파이썬에서 maria db를 접속하고, 쿼리 수행
1. 접속, 해제
2. 쿼리수행 : 쿼리(Query)는 데이터베이스를 조작하는 언어
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
    #####################################################
    # 쿼리 수행 절차
    # 1. 커서 획득
    cursor = conn.cursor()
    # 2. sql 준비
    sql = '''
    select 
	    *
    from 
	    tbl_users
    where 
	    uid='1' and upw=1;
    '''
    # 3. 쿼리 수행
    cursor.execute(sql) 
    # 4. select => 결과 집합이 리턴됨 => 결과 패치
    rows = cursor.fetchall()
    # 멀티라는, 즉 이름만 출력되게 작성
    print(rows)
    for row in rows:
        print(row[3])
    #####################################################
    # 디비 닫기
    conn.close()
    print('닫기성공')

except Exception as e:
    print(e)