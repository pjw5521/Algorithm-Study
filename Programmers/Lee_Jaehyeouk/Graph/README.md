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





