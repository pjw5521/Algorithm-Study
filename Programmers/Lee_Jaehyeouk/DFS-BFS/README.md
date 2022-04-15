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

Step1. BFS의 개념을 이용해서 풀었다. 

Step2. 우선 stack의 begin 부터 시작해서 글자가 한 글자 다른 글자를 찾아낸다. 

Step3. 다음 글자르 찾기 위해 넘어갈ㄸ count 를 증가신다. 이 의미는 트리러 생각했을때 depth 가 1 증가 한 것이다.

Step4. 찾은 글자르 다시 stack 에 넣고 반복하면 target 값과 같으면 count 한 것을 반환한다.

<img width="298" alt="스크린샷 2022-04-16 오전 1 16 17" src="https://user-images.githubusercontent.com/60414900/163594832-a4fdac3d-c9e9-4c7d-9a33-ee4700813218.png">


<br/>

## Problem4

문제: 여행경로(https://programmers.co.kr/learn/courses/30/lessons/43164)

### Solution

Step1. 

Step2. 

Step3. 

Step4. 




