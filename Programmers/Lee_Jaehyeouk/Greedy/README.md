# Greedy <br/><br/>

## Problem1

문제: 섬 연결하기 (https://programmers.co.kr/learn/courses/30/lessons/42861)

### Solution

Step 1. Kruskal 알고리즘을 이용했다. 
링크: https://gmlwjd9405.github.io/2018/08/29/algorithm-kruskal-mst.html

Steo 2. 이전 단계에서 만들어지 신자 트리와느 상관없이 무조건 최소 간선만을 선택한다. 다만 사이클을 형성하는 간선은 우선적으로 제외한다.

![스크린샷 2022-04-22 오후 11 01 25](https://user-images.githubusercontent.com/60414900/164729846-8fadf779-2fb3-4193-b9f2-7b5e7ae85f74.png)

Step 3. 그림을 보면 간선의 출발점, 도착점 가중치가 나와있다. 여기서 Kruskal 을 이용해보면 우선 0 에서 시작하는 가장 가중치 낮은 노드를 선택한다
- 0 에서 시작할때 가 수 있는 노드중 가중치가 가장 낮은 노드 선택
- 0 -> 1
- 그 다음 1에서 갈 수 있는 노드 중 싸이클을 만들지 않는 선에서 가장 가중치가 낮은 노드 선택
- 1 -> 3
- 반복 한다.

<br/>

## Problem2

문제: 단속카메라 (https://programmers.co.kr/learn/courses/30/lessons/42884)

### Solution

Step 1. 출발 지점을 중심으로 풀었다. 우선 차량들으 출발 시점을 기준으로 리스트를 소팅하였다. 그러면 리스트는 출발이 빠른 순으로 정렬 된다.

Step 2. 문제르 예시로 들면 [[-5, -3], [-14, -5], [-18, -13], [-20, -15]] 리스트가 생성된다.

<img width="304" alt="스크린샷 2022-04-23 오전 12 09 52" src="https://user-images.githubusercontent.com/60414900/164742714-771616ad-d4ef-436e-9e9c-fe3e09cc4ea7.png">

Step 3. 그림을 보면 우선 -5에 하나의 카메라를 설치하고 순차적으로 카메라의 위치를 비교한다. 카메라의 도착점이 만약 현재 카메라의 위치보다 작으면 차가 주행한 위치가 단속 카메라보다 뒤에 있다는 것이기 때문에 단속 카메라를 하나 추가한다.

<br/>



