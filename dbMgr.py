'''
파이썬에서 maria db를 접속하고, 쿼리 수행
1. 접속, 해제
2. 쿼리수행 : 쿼리(Query)는 데이터베이스를 조작하는 언어
   conn.cursor()는 pymysql에서 쿼리 수행을 위해서 사용하는 객체임
3. 기본 커서는 데이터를 오직 순서대로만 보내기 때문에 
   테이블 컬럼의 위치가 변경되거나, 쿼리문이 조정되면
   순서가 바뀌게 되서 소스를 수정해야하는 상황이 벌어진다
   => 해결방안 : 컬럼이 따라와서 딕셔너리 형태로 가면 순서가 의미 없으므로 자동으로 해결된다
4. 쿼리문에 인자를 전달하여 수행하기 -> 일반화 기본작업
5. with문을 이용하여 커서 닫기를 자동으로 처리
6. 함수화를 통해서 누구나, 여러번 호출만으로 이 기능을 사용하게 처리
7. 함수에 리턴값을 부여하여 쿼리 결과를 돌려주게 처리
8. 모듈화를 위한 처리
'''
'''
pip install DBUtils
DBUtils의 풀링 기술을 이용하여 전체적으로 쿼리 처리 업그레이드
'''
import pymysql as my
from DBUtils.PooledDB import PooledDB
#from service.model import PostModel

class PostModel:
    title = None
    content = None
    writer = None
    file = None
    def __init__(self, title, content, writer, file):
        self.title = title
        self.content = content
        self.writer = writer
        self.file = file

DB_URL = 'localhost'
DB_PORT = '3306'  #포트가 다른 사람은 변경
DB_USER ='root'
DB_PASSWORD ='1419'
DB_DATABASE ='pythondb'
DB_CHARSET ='utf8'
MAX_POOL = 100

class DBHelper:
    # 멤버 변수
    app = None
    # 풀링 객체(디비와 연결된 커넥션을 가지고 있는 객체)
    connectionPool = None
    # 생성자
    def __init__(self, application=None):
        self.app = application
        if self.app:  # Flask 객체가 존재하면 -> 환경변수에서 뽑아서 세부
            DB_URL = self.app.config['DB_URL']
            #DB_PORT = self.app.config['DB_PORT']
            DB_USER = self.app.config['DB_USER']
            DB_PASSWORD = self.app.config['DB_PASSWORD']
            DB_DATABASE = self.app.config['DB_DATABASE']
            DB_CHARSET = self.app.config['DB_CHARSET']
            MAX_POOL = self.app.config['MAX_POOL']

        self.initPool()
    # 소멸자
    # def 객체명
    def __del__(self):
        self.freePool()
    # 멤버 함수
    # 커넥션 풀 생성
    def initPool(self):
        # MAX_POOL 개수만큼 디비와 커넥션을 생성한다
        self.connectionPool = PooledDB(  creator=my,
                                    host=DB_URL,
                                    user=DB_USER,
                                    password=DB_PASSWORD,
                                    database=DB_DATABASE,
                                    autocommit=False,
                                    charset=DB_CHARSET,
                                    cursorclass=my.cursors.DictCursor,
                                    blocking=False,
                                    maxconnections=MAX_POOL
                                  )
        
    # 커넥션 풀 해제
    def freePool(self):
        # 디비와 연결된 모든 커넥션을 닫는다
        self.connectionPool.close()
        
    # 개별쿼리
    
    # 로그인 처리
    def loginSql(self, uid, upw):
        rows = None
        try:
            # 커넥션을 풀링해서 빌려온다
            conn = self.connectionPool.connection()
            # 쿼리 수행 ===================================
            cursor = conn.cursor()
            sql = '''
                select
                    * 
                from
                    tbl_users
                where
                    uid=%s and upw=%s;
            '''
            cursor.execute(sql, (uid, upw))
            rows = cursor.fetchone()
            cursor.close()
            # =============================================
            # 풀링에 반납한다
            conn.close()
        except Exception as e:
            rows = None
        return rows

    # 검색 처리
    def searchSql(self, keyword):
        rows = None
        try:
            # 디비 오픈
            conn = self.connectionPool.connection()
            # 쿼리
            cursor = conn.cursor()
            sql = "select rank, name from tbl_epl where name like '%{0}%';".format(keyword)
            cursor.execute(sql) 
            rows = cursor.fetchall()
            cursor.close()
            # 디비 닫기
            conn.close()
        except Exception as e:
            rows = None
        return rows

    # 팀 검색
    def selectTeamName(self, teamName):
        rows = None
        try:
            # 디비 오픈
            conn = self.connectionPool.connection()
            # 쿼리
            cursor = conn.cursor()
            sql = "select * from tbl_epl where name=%s;"
            cursor.execute(sql, (teamName,)) 
            # fetchone() 1개만 가져온다 => 리스트 형태 제외됨
            rows = cursor.fetchone()  
            cursor.close()
            # 디비 닫기
            conn.close()
        except Exception as e:
            rows = None
        return rows
        
    # 팀 정보 수정(총 경기수만 수정)
    def updateTeamInfo(self, total, teamName):
        result = None
        try:
            # 디비 오픈
            conn = self.connectionPool.connection()
            # 쿼리
            cursor = conn.cursor()
            sql = "update tbl_epl set total=%s where name=%s;"
            cursor.execute(sql, (total, teamName))
            # 커밋(디비에 실제 반영)
            conn.commit()

            # 영향받은 로우수로 설정 = 수정된 row의 수
            result = conn.affected_rows()
            cursor.close()
            # 디비 닫기
            conn.close()

        except Exception as e:
            result = None
        
        finally:
            return result
        
    # 모든 팀 가져오기
    # (정렬기준 컬럼, 정렬방식, 시작페이지, 한 페이지의 양)
    def selectAllEplList(self, stdCol='rank', order='asc', page=0, amt=5):
        rows = None
        try:
            # 디비 오픈
            conn = self.connectionPool.connection()
            # 쿼리
            cursor = conn.cursor()
            sql = '''select rank, name, winPoint, win from tbl_epl 
            order by %s %s 
            limit %s, %s;''' %(stdCol, order, page, amt)
            cursor.execute(sql) 
            rows = cursor.fetchall()
            cursor.close()
            # 디비 닫기
            conn.close()

        except Exception as e:
            print(e)
            rows = None
        #else
        
        finally:
            return rows

    # 게시물 모두 가져오기
    def selectAllBbs(self): pass

    # 게시물 등록
    def insertPost(self, postModel):
        result = None
        try:
            # 디비 오픈
            conn = self.connectionPool.connection()
            # 쿼리
            cursor = conn.cursor()
            sql = "insert into tbl_bbs(title, content, `file`, writer, regdate) values (%s, %s, %s, %s, now())"
    
            cursor.execute(sql, (postModel.title, postModel.content, postModel.file, postModel.writer))
            # 커밋(디비에 실제 반영)
            cursor.close()
            conn.commit()

            # 영향받은 로우수로 설정 = 수정된 row의 수
            #result = conn.affected_rows()
            
            # 디비 닫기
            conn.close()

        except Exception as e:
            result = None
        
        finally:
            return result


# 테스트 코드는 if문 이하로 이동 : 모듈화 처리 중 불필요한 코드 이동
if __name__ == '__main__':
    #results = selectTeamName('번리 FC')
    #results = updateTeamInfo('1000','번리 FC')
    #results = selectAllEplList()
    #print('결과 :', results)
    obj = DBHelper()
    #print(obj.loginSql('1','1'))
    param = PostModel('제목1', '내용1', '작성자1', '파일경로1')
    print(obj.insertPost(param))
    #pass
    import os
    print(os.getcwd())