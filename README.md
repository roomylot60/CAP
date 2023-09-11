# CAP(Common Alerting Protocol)
## 23.09.11 Before starting project
### 시작하게 된 계기
1. 학부 재학 중 진행하던 프로젝트를 리펙토링 해보고자 함
2. 기존 프로젝트의 경우 WS를 구현해보았다면, WAS를 사용해 재구성해보고자 함
3. Django, MySQL, Docker의 기능을 활용한 프로젝트를 제작해보고자 함
### 사용할 기술
- Frontend
    - HTML
    - Node.js
    - JSON
- Backend
    - DJango
    - Docker
- Database
    - MySQL
---
## Initializing project
### 23.09.11
- DJango를 활용해 project 생성
- App 2가지 작성 : acounts, Common_Alerting_Protocol
- 이전에 진행했던 html 파일을 기본 templates로 생성
- settings.py 수정
    - App 리스트 목록 추가
    - BASE_DIRS와 같은 변수 초기 조정
    - DATABASE 부분은 추후 추가 후 수정 예정
    - STATIC_URL 수정
- 초기 제작한 프로젝트 git을 통해 연결