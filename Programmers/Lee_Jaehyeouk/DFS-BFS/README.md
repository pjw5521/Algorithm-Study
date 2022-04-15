# BFS-DFS <br/><br/>

## Problem1

문제: 타겟 넘버 (https://programmers.co.kr/learn/courses/30/lessons/43165)

### Solution

Step 1. BFS를 이용하여 풀었다.

Step 2. 문제에서는 더하기, 뺄셈만 가능하기 때문에 고려해야 할것은 두가지 뿐이다.

Step 3. numbers의 숫자르 하나씩 뽑아 계산이 가능한 모든 경우의 수를 순차적으로 리스트에 추가한다.

Step 4. 완서 된 리스트에서 target 과 비교하여 count 한다.

<br/>

## Problem2

문제: 네트워크 (https://programmers.co.kr/learn/courses/30/lessons/43162)

### Solution

Step 1. DFS를 이용하여 풀었다.

Step 2. [False] * n 을 만들어 방문한 노드르 True 로 만든다.

- 문제를 예시로 들자면 우선 [False, False, False]를 생성 한다. 
- 첫번째 노드를 방문하여 True 로 만들고 연결되어 있느 노드도 True로 만든다.
- 그럼 1번 노드의 경우 2번 노드와 붙어 있기 때문에 한번의 DFS를 돌고 나오면 visited = [True, True, False] 가 되고 answer = 1 이 된다.
- 그럼 네트워크 1개가 생성 된것이고 이것을 반복한다.

<br/>

## Problem3

문제: 단어변환(https://programmers.co.kr/learn/courses/30/lessons/43163)

### Solution

Step1. 

Step2. 

Step3. 

Step4. 

<br/>

## Problem4

문제: 여행경로(https://programmers.co.kr/learn/courses/30/lessons/43164)

### Solution

Step1. 

Step2. 

Step3. 

Step4. 




