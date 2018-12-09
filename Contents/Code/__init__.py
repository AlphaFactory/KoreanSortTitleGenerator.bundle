from datetime import datetime
from dateutil.parser import parse
from difflib import SequenceMatcher
import os, re, sys, traceback, urllib, urlparse

def Start():
    pass

class KoreanSortTitleGenerator(Agent.Movies):
    """
    한국어 정렬명 생성용 보조 에이전트
    (Korean Sort Title Generator)

    Plex Media Server에서는 한국어 정렬을 완전히 지원하고 있지 않다.
    스크롤바 오른쪽을 보면 자음이 아니라 첫 글자순으로 배열되어 있음을 알수 있다.
    본 에이전트는 정렬명을 자동으로 수정하여 이 것이 자음 순으로 배열되도록 수정해준다.
    대량의 영화를 관리하는 사람이라면 반드시 필요할 것.
    """
    name = 'Korean Sort Title Generator'
    ver = '1.0'
    primary_provider = False
    languages = [Locale.Language.NoLanguage]
    contributes_to = [
        'com.plexapp.agents.imdb',
        'com.plexapp.agents.themoviedb',
        'com.plexapp.agents.xbmcnfo',
    ]

    def get_sorttitle(self, title):

        # Plex Media Server는 Python 2 기반이라 유니코드 관련으로 문제가 좀 있음.
        # 해결책을 찾기 전까진 아래와 같이 하드코딩 예정
        FIRST_LETTERS = [ "가", "나", "다", "라", "마", "바", "사", "아", "자", "차", "카", "타", "파", "하" ]
        CONSONANTS = [ "ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ" ]
        LAST_LETTER = "힣"

        # 본래 영화제목 첫글자
        first = title.decode("utf-8")[0]

        # 제목이 한국어로 시작하는지 체크
        if first >= FIRST_LETTERS[0] and first <= LAST_LETTER:
            for i in range(0, 13):
                if i < 13:
                    if first < FIRST_LETTERS[i+1]: return CONSONANTS[i] + title
            return CONSONANTS[13] + title
        else:
            return title

    # Search 함수
    def search(self, results, media, lang, manual=False):
        # 여타 주요 에이전트에서 넘어온 데이터에 100점을 주고 사용
        if media.primary_metadata:
			results.Append(MetadataSearchResult(id = media.primary_metadata.id, score = 100))

    # Update 함수
    def update(self, metadata, media, lang, force=False):
        if metadata.title:
            metadata.title_sort = self.get_sorttitle(metadata.title)
        else:
            metadata.title_sort = self.get_sorttitle(media.title)
