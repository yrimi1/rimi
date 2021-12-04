##################### 126. 개발 환경 구축 #####################

## 하드웨어 =  클라이언트와 서버 로 구성
# 클라이언트는 사용사와의 인터페이스역할 ex)스마트폰, PC
# 서버는 클라이언트와 통신
# 서버는 (사용 목적에 따라서 ): 웹서버 ,웹어플 ,db,파일
# 웹서버 : 클라이언트한테 직집요청받아 처리.. http ,구글등이 해당..정적파일
# 웹어플서버(was): 사용자에게 동적 서비스 제공,웹서버에서 정보받아 처리가공 ,
#                웹서버와 db 혹은  웹서버와 파일서버 사이에서 인테페이스 역할하는 서버
#                톰켓 ,웹 스피어 ,오라클웹로직 등이 해당..
# db서버 : db관리, DBMS운영... SQL .오라클 
# 파일서버 : db에 쓰기 비효율적인 파일 저장, 서비스제공목적 AWS S3 (아마존 웹 서비스 심플 스트롱 서비스) 가 있다

#정적파일 : 브라우저 에서 별도 처리 없이 사용가능(html,css)
#동적서비스 : 사용자의 입력에 따라 달라지는 화면 
# 웹서버의 기능
# http응답,로그기록 ,css저장관리 ,대역폭제한, 가상 호스팅 서버에 여러도매인 연결 , 인증


## 소프트웨어 = 시스템소프트웨어 와 개발소프트웨어
# 시스템 소프트웨어는 클라이언트와 서버 운영한다 , 운영체제 OS, DBMS가있음
# 개발 소프트웨어는 개발한다 , 요구사항관리, 설계 모델링 , 구현 ,빌드 , 테스트, 형상관리