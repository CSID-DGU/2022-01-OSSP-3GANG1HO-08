from asyncio.windows_events import NULL
from neo4j import GraphDatabase
import pandas as pd

contextlist = ['코드', '반복', '컴파일러', '이중', '입력', '입출력', '출력', '문자', '다차', '유형', '파일', '저장', '연산', '프로그램', '처리', '메모리', '분할', '산술', '자료형', '포인터',
'개방', '사용', '논리 연산', '공용', '선언', '방법', '개념', '영역', '수 문자', '부록', '모음', '아스키', '버퍼', '언어', '문자열', '변수', '할당', '표현', '함수', '기본', '사용자', '정복', 
'알고리즘', '구조', '완전', '연산자', '작성', '공간', '데이터', '사용법', '선택 정렬', '활용', '이해', '컴파일', '관계', '선택', '함수 포인터', '가지', '응용', '배열', '상수', '공유', '동적', '코드', 
'이중', '이진 탐색 트리', '처리', '다항식', '수식', '포인터', '이진 트리', '해시', '정의', '하노이', '이닝', '트리', '동적 메모리 할당', '순회', '선택 정렬', '비교', '순환', '정렬 알고리즘', 
'표기', '최단', '예제', '삽입 정렬', '선형', '재생', '개방', '스레드 이진 트리', '연습', '동적 배열', '후위', '우선순위 큐', '타입', '비용', '계산', '버퍼', '추가', '연결 리스트', '그래프', '소개', 
'표현', '용량', '함수', '너비 우선 탐색', '피보나치 수', '성능', '버블', '배열', '시뮬레이션', '원형', '스택', '디렉토리', '문제', '거듭제곱', '프로그램', '위상', '히프', '자료', '신장', '개념', 
'용어', '레벨', '스케줄링', '구현', '정렬', '리스트', '영어', '허프', '알고리즘', '분석', '경로', '데이터', '탐색', '최소', '응용', '반복', '연산', '추상', '사전', '미로', '사용', '방법', 
'합병 정렬', '검사', '분야', '퀵 정렬', '희소행렬', '구조', '추상 자료형', '괄호', '주소', '깊이 우선 탐색']

totagdic = {'입출력': ['입력','출력'], '연산': ['연산자','논리 연산','산술','분할'], '정렬': ['정렬 알고리즘','버블','퀵 정렬','합병 정렬','삽입 정렬','선택 정렬'], '그래프': ['연결 리스트','너비 우선 탐색',
'피보나치 수','이진 트리', '스레드 이진 트리']}

def add_context(tx, title, tag):
  tx.run("MERGE (a:Context {title: $title, tag: $tag})", title=title, tag=tag)

def add_tag(tx):
  tx.run("MATCH (a:Context) " 
  "UNWIND a.tag as k "
  "MERGE (b:Tag {name:k}) " 
  "MERGE (a)-[r:Contain]->(b)")

greeter = GraphDatabase.driver("bolt://localhost:7687", auth=("pgrgrgrgr", "ossptest"))

with greeter.session() as session:
  for key in totagdic.keys():
    session.write_transaction(add_context, title=key, tag=totagdic[key])
  session.write_transaction(add_tag)

    