##  가장 먼 노드<br/><br/>

### Problem 
https://programmers.co.kr/learn/courses/30/lessons/49189

### Solution

Step 1. bfs를 이용하여 풀었습니다.<br/><br/>
- 여기서 중요한것은 distance(방문한 노드 간선 수)를 구하기 위해서 맨 처음 -1을 넣어서 시작해야 합니다.
- https://www.youtube.com/watch?v=7C9RgOcvkvo 

Step 2. node를 인접리스트로 생성합니다.그 후 bfs를 통해 노드 1에서 시작 했을 때 각 노드별로 거리를 계산한 distance를 반환합니다. <br/><br/>

Step 3. 노드 1(조건)부터 시작해서 BFS로 탐색하며 몇번을 거쳐 왔는지 count를 q에 정점과 같이 넣어서 진행했습니다.<br/><br/>

Step 4. visited 라는 리스트에 각 인덱스(노드)에 count 를 넣고 몇번 지났는지 계산했습니다.<br/><br/>

Step 5. distance 안에 max 값의 갯수를 세서 반환합니다.


