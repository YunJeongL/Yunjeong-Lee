'''
파이썬에서 maria db를 접속하고, 쿼리 수행
1. 접속, 해제
2. 쿼리수행 : 쿼리(Query)는 데이터베이스를 조작하는 언어
3. 기본 커서는 데이터를 오직 순서대로만 보내기 때문에 
   테이블 컬럼의 위치가 변경되거나, 쿼리문이 조정되면
   순서가 바뀌게 되서 소스를 수정해야하는 상황이 벌어진다
   => 해결방안 : 
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
    # 1. 커서 획득 : my.cursors.DictCursor 추가
    cursor = conn.cursor(my.cursors.DictCursor)
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
        print(row['name'])
    #####################################################
    # 디비 닫기
    conn.close()
    print('닫기성공')

except Exception as e:
    print(e)