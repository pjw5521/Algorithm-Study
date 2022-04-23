# Algorithm 개념 정리 

### 문제 풀이 사이트
- 프로그래머스 : https://programmers.co.kr

## 1. 해시(Hash)
- 데이터를 다루는 기법 중 하나로, key-value 형태로 데이터를 저장한다.
- **해싱(Hashing)**
    - 키에 대한 해시값을 구하는 과정
- **해시 함수(hash function)**
    - 데이터를 일정한 길이의 비트열(해시값)로 변환시켜주는 함수
- key를 해시 함수를 통해 임의의 값으로 변경한 뒤 배열의 인덱스로 변환하여 해당하는 값에 데이터를 저장한다. 
- key 값이 배열의 인덱스로 저장되기 때문에 검색과 저장이 매우 빠르다.
- 평균 시간 복잡도 : O(1)
- **딕셔너리**
    - 파이썬에서는 해시 테이블을 딕셔너리로 표현
    - key와 value를 한 쌍으로 가지는 자료형 : { key1 : value1, key2 : value2, ... }
    - 예시 
     ```python
     dic = dict() # 딕셔너리 선언 
     dic['a'] = 10 # key 'a'에 대한 value 값 10 
     
     print(dic.keys()) # key만 출력
     print(dic.values()) # value만 출력
     print(dic.items()) # key, value 모두 출력 
     print(dic['a']) # 10 출력 
     ```
    - 정렬 : sorted 사용 
    
## 2. 힙(Heap)
- 완전 이진 트리의 일종으로, **우선순위 큐**를 위해 만들어진 자료구조 
- 최댓값이나 최솟값을 빠르게 찾을 수 있다. 시간복잡도 O(1)
- 최대 힙 (Max heap)
    - 부모노드의 값이 자식노드의 값보다 큰 힙 
- 최소 힙 (Min heap)
    - 부모노드의 값이 자식노드의 값보다 작은 힙 
- 파이썬에서는 최소 힙 자료구조 제공 
    + **import heapq**
    + 원소들이 항상 정렬된 상태로 추가되고, 삭제 
    + 가장 작은 원소가 제일 앞에 추가
    + 가장 작은 원소가 제일 먼저 삭제 
    + 원소 추가 : heapq.heappush( 리스트 이름, 원소 )
    + 원소 삭제 : heapq.heappop( 리스트 이름 ) 