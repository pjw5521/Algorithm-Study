##  이중 우선순위 큐<br/><br/>

### Problem 
https://programmers.co.kr/learn/courses/30/lessons/42628. 

### Solution

Step 1. Heap을 이용했습니다.

Step 2. 우선 operations으로 들어온 string 값을 split을 통해서 구분 짓고 해당 명령어에 따라 조건문을 설정했습니다.  

Step 3. 명령어에 따른 수행 연산에 대해서 어떠한 함수를 사용할지 정리했습니다.  
- I: Heap에 숫자 삽입 (heappush)  
- D1: Heap에서 최대값을 삭제 (nlargest 이용)  
- D -1: Heap에서 최소값을 삭제 (heappop)  

Reference: https://docs.python.org/ko/3/library/heapq.html

Step 4. 문제에 나와있는 몇가지 조건에 대해서도 조건을 걸어줍니다.
- 빈큐에 데이터를 삭제하는 연산이 주어질 경우 무시한다.
- 처리한 큐가 비어 있으면 [0,0]을 반환한다.
