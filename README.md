# KoreanSortTitleGenerator.bundle
Plex Media Server 한국어 정렬명 생성용 보조 에이전트(Secondary Agent)

Plex Media Server에서는 한국어 정렬을 완전히 지원하고 있지 않다.  
스크롤바 오른쪽을 보면 자음이 아니라 첫 글자순으로 배열되어 있음을 알 수 있다.  
본 에이전트는 정렬명을 자동으로 수정하여 이 것이 자음 순으로 배열되도록 수정해준다.  
대량의 영화를 관리하는 사람이라면 반드시 필요할 것.  

## 설치 방법
1. [에이전트 압축파일](https://github.com/AlphaFactory/KoreanSortTitleGenerator.bundle/archive/master.zip)을 다운받는다.
2. 압축을 풀면 폴더 제목이 KoreanSortTitleGenerator.bundle-master가 되어 있을 것이다. 뒤의 "-master"부분을 삭제한다.
3. 폴더를 $PLEX_HOME\Library\Application Support\Plex Media Server\Plug-ins에 이동한다.
4. Plex Media Server를 재시작한다.
5. 설정의 에이전트 메뉴로 가서 Plex Movie나 The Movie Database, XBMCnfoMovieImporter 탭에 "Korean Sort Title Generator"가 있는지 확인한다.
6. 체크하여 활성화 해준다.
