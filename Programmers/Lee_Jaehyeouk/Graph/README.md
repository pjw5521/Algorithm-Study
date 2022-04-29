# Graph <br/><br/>

## Problem1

문제: 방의 갯수 (https://programmers.co.kr/learn/courses/30/lessons/49190)

### Solution

Step 1. 우선 방이 생기는 조건에 대해서 생각했다.

[그림1]
- 우선 방문한 노드를 재 방문 해야 한다.
- 재 방문한 노드가 기존에 만들어진 간선이 아니어야 한다.
<img width="175" alt="스크린샷 2022-04-23 오전 12 59 07" src="https://user-images.githubusercontent.com/60414900/164751490-17e07dae-6213-4c40-acbf-ca3b4b4e7bc8.png">


[그림2]
- 하지만 숨은 함정이 있는데 바로 모래 시계 형태이다. 
- 그렇기 때문에 모든 뱡향에 움직임들에 대해서 2번씩 실행 되어야 한다.
<img width="208" alt="스크린샷 2022-04-23 오전 1 08 43" src="https://user-images.githubusercontent.com/60414900/164753017-69fc46b6-2650-4d16-84a6-83f83a4a75d9.png">



Step 2. 우선 움직임에 대해 move르 만들고 방문한 노드와 그에 대한 경로를 dic에 저장한다.

Step 3. 모래시계를 대비하여 해당 방향으로 2칸을 더 간것으로 간주하고 추간한다. 

Step 4. 이제 큐를 돌며 그래프가 생기는 조건에 대해서 만족하면 answer + 1 시킨다. 

<br/>

##  가장 먼 노드<br/><br/>

### Problem2
https://programmers.co.kr/learn/courses/30/lessons/49189

### Solution

Step 1. bfs를 이용하여 풀었습니다.
- 여기서 중요한것은 distance(방문한 노드 간선 수)를 구하기 위해서 맨 처음 -1을 넣어서 시작해야 합니다.
- https://www.youtube.com/watch?v=7C9RgOcvkvo <br/><br/>

Step 2. node를 인접리스트로 생성합니다.그 후 bfs를 통해 노드 1에서 시작 했을 때 각 노드별로 거리를 계산한 distance를 반환합니다. <br/><br/>

Step 3. 노드 1(조건)부터 시작해서 BFS로 탐색하며 몇번을 거쳐 왔는지 count를 q에 정점과 같이 넣어서 진행했습니다.<br/><br/>

Step 4. visited 라는 리스트에 각 인덱스(노드)에 count 를 넣고 몇번 지났는지 계산했습니다.<br/><br/>

Step 5. distance 안에 max 값의 갯수를 세서 반환합니다.







