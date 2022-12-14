# Toy Project 1: Okky Dokky(v1.0)

# Project 개발 배경

이 프로젝트는 Python을 첫 언어로 입문하여 Django Web Framework로 제작한 프로젝트입니다.

코딩에 입문하는 또는 영어가 익숙하지 않은 사용자가 부담없이 이용할 수 있는 국내판 Stack Overflow인 (주)오키코리아 사의 [Okky.kr](http://Okky.kr) 사이트를 사용자 친화적으로 한 번 더 재 가공하여 만든 프로젝트입니다.

- 2022년 8월 22일부로 okky의 자사 웹사이트 완전 개편(v1.0에서 v2.0로)으로 인하여 해당 프로젝트를 위해 만들어 놓은 수집코드(크롤러)는 현재 사용할 수 없습니다.
- 이미 수집한 데이터(20만여개) 8월 9일자 까지는 Database에 저장해 놓은 상태입니다.
- v2.0에 맞는 데이터 수집 코드를 수정 중에 있습니다.

# 환경

1. **사용된 언어**
    1. Python(Version: 3.2.13)
    2. JavaScript(jQuery(Version: 3.4.1))
    3. HTML
2. **사용된 웹 프레임워크**
    1. Django (Version: 3.0.14)

# 목표

1. **파싱 (Parsing) :**
    
    Okky 사이트 내 Tech Q&A 게시판(8,000 페이지 이상) 및 게시글 데이터(20만 개  이상)를 크롤링(Crawling)하여 가공한 뒤 Django 데이터 베이스에 저장.
    
2. **선별 :**
    
    추후 업데이트 용이성 및 정보 제공의 우선 순위를 위하여 Okky 사이트 내 Tech Q&A 게시판에서 댓글이 없는 게시글, 댓글이 있는 게시글, 채택된 댓글이 있는 게시글로 구분하여 데이터를 수집.
    
3. **페이지네이션:**
    
    Django 내장 페이지네이터(Paginator) 사용 없이 페이지네이션(Pagination) 구현.
    
4. **업데이트 :**
    
    일정 주기로 최근 200 페이지(약 30일 분량)를 윈도우 작업 스케줄러에 Weekly Update Code를 등록하여 업데이트를 진행.
    
5. **비동기 게시판:**
    
    JQuery 사용으로 비동기 식으로 게시판 구현.
    
6. 배포:
    
    AWS Elastic Beanstalk 서비스를 이용하여 배포.
    

# 차별점

1. **비동기 게시판:**
    
    비동기 게시판으로 구성하여 페이지 전환 없이, show(), hide() 이벤트를 통해 답변과 채택 답변을 볼 수 있게 만들었습니다.
    
2. **선별:**
    
    빠르고 정확한 정보 검색을 위하여 댓글이 없는 게시글은 배제하며, 채택된 댓글이 있는 게시글을 우선 순위로 배치합니다.
    
3. **코드 언어 판별:**
    
    게시글에 코드 블록(Code Block)이 사용되었다면, 사용된 해당 코드 블록의 언어(c, cpp, python, java, 등)를 추출하여, OkkyDokky 게시판 내 게시글 제목 하단에 태그(Tag) 형식으로 미리 보기를 지원합니다.
    
4. **내용:**
    
    게시글의 내용에 이미지, 코드, 또는 이미지와 코드가 모두 사용되었는지, OkkyDokky 게시판 내 게시글 제목 옆에 미리 보기를 지원합니다.
    
5. **검색식 선택(AND 또는 OR):**
    
    AND와 OR 조건의 검색식을 적용하였습니다. (선택 가능)
    
6. Dash Board 구현:
    
    Toast UI를 이용한 Chart Dash Board 구현.
    

# 과정

1. **데이터 수집 (약 35시간 소요)**
    1. 게시판은 한 페이지 당 24개의 게시글이 노출되며, Query string의 offset 값으로 페이지 전환을 시켜줍니다. 
        
        [https://okky.kr/articles/questions?offset=1&max=24&sort=id&order=desc](https://okky.kr/articles/questions?offset=0&max=24&sort=id&order=desc)
        
        (1 페이지 : offset=1,  2 페이지 : offset=24, 3 페이지 : offset=48)
        
    2. 게시글 URL 수집
        
        게시판에서 게시글로 이동을 위해 게시판의 <li> 태그 내의 각 게시글의 URL를 수집합니다.
        
    3. 게시글 정보 수집:
        1. 게시글 제목
        2. 댓글 수
        3. 게시글 게시 날짜
        4. 게시글 내용
        5. 게시글 내용 구성 (Text, Code, Image)
        6. 게시글 코드 언어
        7. 게시글 채택 답변
        8. 게시글 채택 답변 게시 날짜
2. 배포
    1. AWS - Elastic Beanstalk를 통해 배포
    2. 가비아 도메인 구입 후 AWS - Route 53와 연결

# 프로젝트 중 문제점 및 해결 과정

1. **Crawling 중단 현상**
    
    게시글 크롤링 중 패턴이 없는 중단 현상을 발견하여, 코드의 문제는 아닐 것이라는 판단을 하고, 일단 해당 URL들은 따로 container에 담아 두고 추후 살펴보기로 하였습니다. 해당 오류는 예외 처리를 하여 계속하여 크롤링을 진행하였습니다.
    
    해결: Container에 저장해둔 URL을 다시 크롤링을 해봤지만 처음부터 돌아가지 않았으며, 해당 URL을 접속해보니 Okky 서버의 문제로 에러 메세지를 표시하며 게시글 내용을 볼 수 없었습니다.
    
    크롤러는 게시글 제목부터 크롤링하기에 해당 게시글은 제목이 없으므로 오류가 난 것으로 결론지었습니다.
    
2. **데이터 로딩 속도 저하**
    
    해결: datetime.now()을 사용하여 코드 중간, 중간에 심어 오래 걸리는 구간을 파악하였습니다. totalPage를 구하려 len()을 사용했었는데, count()로 변경 후에 해결했습니다.
    

# 관리

일정 주기로 최근 100 페이지(약 15일 분량)를 윈도우 작업 스케줄러에 update code를 등록하여 업데이트를 진행 (약 30분 소요).

1. 새로 등록된 게시글 크롤링
2. 답변이 없던 게시글에 답변이 등록 되었다면 수집.
3. 채택된 답변이 없던 게시글에 채택된 답변이 등록 되었다면 수집.

# 개선 필요 사항

1. okky 사이트 개편으로 인하여 v2.0에 맞는 데이터 수집 코드를 수정 중입니다.

# 구현한 사이트

1. 메인 페이지

![Screenshot 2022-10-05 at 19 18 30](https://user-images.githubusercontent.com/102448185/194038944-b5725a4b-c14c-4600-a1ef-b6393cb97e44.jpg)

2. 게시판 페이지

![Screenshot 2022-10-05 at 19 16 38](https://user-images.githubusercontent.com/102448185/194038997-5b8c8590-b2b2-4227-9b4d-c3ab6c4426b5.jpg)

3. 마이 페이지

![Screenshot 2022-10-05 at 19 17 09](https://user-images.githubusercontent.com/102448185/194039028-62b2aa9c-5a87-46a6-9f9c-511b9eed4b60.jpg)

4. 검색, N개씩 보기, 태그 정렬

![Screenshot 2022-10-05 at 19 22 05](https://user-images.githubusercontent.com/102448185/194039110-a859886a-a4e3-4e25-8233-9a1b3f43ba7c.jpg)

![Screenshot 2022-10-05 at 19 21 16](https://user-images.githubusercontent.com/102448185/194039129-2f6d21bf-1dd2-4d90-a27b-f610d25dbc6b.jpg)

![Screenshot 2022-10-05 at 19 21 42](https://user-images.githubusercontent.com/102448185/194039193-b5991da5-027e-4e1f-b1c3-9adb806bea29.jpg)

