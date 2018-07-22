py_cmsEx : 구조개선, 요청 및 응답에 대한 사전/사후 처리,
           쿠키 도입, 디비 연결 및 종료 개선 처리, 
           API 기능 추가(json기반), 블루프린트(고민)
------------------------------------------------------------------------------
static : 정적 폴더, css, js, image, 파일업로드 저장위치
        라우트 없이 url이 자동부여
        http://ip:port/static/xxx.xxx
        정적 폴더를 변경할 수 없는가? -> 가능하다
------------------------------------------------------------------------------
templates : render_template()에서 사용하는 html 파일이 위치함
------------------------------------------------------------------------------
run.py : 프로그램의 시작점, 서버의 시작점 
------------------------------------------------------------------------------
session : 사이트에 로그인한 유저의 특정 경로를 저장하여 서버가 관리한다.
        세션이 유지되는 동안 로그인한 것으로 간주
        특정 페이지 접근 허락한다. 동접이 크면 DB쪽에 저장하지만,
        대량 유저가 동접하는 규모가 아니면, 서버 메모리에 저장하여 관리한다
------------------------------------------------------------------------------
<-> cookie : 유저 브라우저에 저장하는 정보 (대표적인 것 -> 아이디 저장)
------------------------------------------------------------------------------
파일업로드 : ~/bbs/upload -> get -> 폼
            ~/bbs/upload -> post -> 등록
            ~/bbs        -> get -> 등록된 글 리스트
------------------------------------------------------------------------------
1) service > controller > __init__.py에 blueprint 정의
2) service > __init__.py에 blueprint 등록
        from .. import bp_bbs
        app.register_blueprint(bp_bbs, url_prefix='/bbs')
3) service > controller > bbs.py 생성
   service > __init__.py에 bbs import
   from service.controller import user, epl, bbs
   from service.controller import bp_user, bp_epl, bp_bbs
4) 테이블 생성 및 spl 테스트
CREATE TABLE `tbl_bbs` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`title` VARCHAR(50) NULL DEFAULT NULL,
	`content` TEXT NULL DEFAULT NULL,
	`file` VARCHAR(512) NULL DEFAULT NULL,
	`writer` VARCHAR(50) NULL DEFAULT NULL,
	`regdate` DATETIME NULL DEFAULT '',
	PRIMARY KEY (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;
-- 게시물 하나 추가하기 
insert into tbl_bbs(title, content, `file`, writer, regdate) values ('제목', '내용', 'upload/img/sss.jpg', '1', now()) 
 
5) service> model> dbMgr.py에 멤버함수 2개 추가
# 게시물 모두 가져오기
def selectAllBbs(): 

# 게시물 등록
def insertPost(postModel): 