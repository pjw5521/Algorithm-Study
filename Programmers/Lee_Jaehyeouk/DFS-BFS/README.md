# BFS-DFS <br/><br/>

## Problem1

문제: 타겟 넘버 (https://programmers.co.kr/learn/courses/30/lessons/43165)

### Solution

Step 1. BFS를 이용하여 풀었다.

Step 2. 문제에서는 더하기, 뺄셈만 가능하기 때문에 고려해야 할것은 두가지 뿐이다.

Step 3. numbers의 숫자르 하나씩 뽑아 계산이 가능한 모든 경우의 수를 순차적으로 리스트에 추가한다.

Step 4. 완성 된 리스트에서 target 과 비교하여 count 한다.

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

Step1. defaultdic을 이용해서 풀었다.

Step2. 우선 ticket을 각 출발을 key 로하여 dictionary를 생성 후 조건에 맞게 정렬한다.

Step3. 시작은 무조건 ICN이기 때문에 stack 이라는 리스트에 넣고 시작한다.

Step4. 반복문을 돌며 stack의 맨 상단에 위치한 값을 tmp에 저장하여 해당 tmp를 key 값으로 갖는 value 가 존재하면 stack에 없으면 answer에 집어넣는다.
- dfs의 개념이다.

Step5. 위 문제를 예시로 들며 진행해보겠다.

세팅 완료  
<img width="402" alt="스크린샷 2022-04-16 오후 12 03 40" src="https://user-images.githubusercontent.com/60414900/163659085-d7653ac8-cc54-42c9-b842-290807bcd10a.png">


반복문 진행  

<img width="523" alt="스크린샷 2022-04-16 오후 12 03 22" src="https://user-images.githubusercontent.com/60414900/163659074-8425e7d4-48d1-40b1-9dd4-6262580a1c28.png">




