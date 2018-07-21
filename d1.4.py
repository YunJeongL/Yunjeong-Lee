'''
파이썬에서 maria db를 접속하고, 쿼리 수행
1. 접속, 해제
2. 쿼리수행 : 쿼리(Query)는 데이터베이스를 조작하는 언어
3. 기본 커서는 데이터를 오직 순서대로만 보내기 때문에 
   테이블 컬럼의 위치가 변경되거나, 쿼리문이 조정되면
   순서가 바뀌게 되서 소스를 수정해야하는 상황이 벌어진다
   => 해결방안 : 컬럼이 따라와서 딕셔너리 형태로 가면 순서가 의미 없으므로 자동으로 해결된다
4. 쿼리문에 인자를 전달하여 수행하기 -> 일반화 기본작업
'''
import pymysql as my

try:
    # 디비 오픈
    conn = my.connect(host='127.0.0.1',
                        #port = '3307'(포트가 다른 사람은 변경),
                        user='root',
                        password='1419',
                        db='pythondb',
                        charset='utf8',
                        cursorclass=my.cursors.DictCursor)
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
	    uid=%s and upw=%s;
    '''
    # 3. 쿼리 수행
    cursor.execute(sql, ('1','1')) 
    # 4. select => 결과 집합이 리턴됨 => 결과 패치
    rows = cursor.fetchall()
    # 멀티라는, 즉 이름만 출력되게 작성
    print(rows)
    for row in rows:
        print(row['name'])
    # 5. 커서 닫기
    cursor.close()
    #####################################################
    # 디비 닫기
    conn.close()
    print('닫기성공')

except Exception as e:
    print(e)