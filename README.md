# weedeyes-21st-server-

## 개발 환경
#### python
- python==3.11.3
#### pip list
- django==4.0
- djangorestframework==3.13.1
- firebase-admin==6.4.0
- django-dotenv 1.4.2
- django-environ 0.11.2

## 커밋 유형

- feat: 새로운 기능 개발 시 사용. 커밋 단위는 구현한 `기능` 단위로 커밋한다.
- fix: 버그 수정
- docs: 문서 작업, README.md와 같은 Markdown 파일 추가 및 변경사항에 대한 업데이트 시 사용한다.
- style: 코드 스타일 조정, 포매팅 과정에 관한 내용을 커밋할 때 사용한다.
    
    EX: 공백과 들여쓰기를 활용한 코드 스타일 정리, 코드에 주석을 추가, 변수 이름을 명확하게 작성
    
- refactor: 기능의 변화는 없지만 성능을 개선하는 과정
    
    EX: `foreach` 대신 `stream` 을 활용한 가독성 및 성능 개선, 중복된 코드를 개선, 클래스를 분리, 함수의 파라미터 재구성
    
- test: 테스트 코드 추가 시 사용
- chore: 빌드 관련 파일 수정 시 사용 (yml, gradle 등)