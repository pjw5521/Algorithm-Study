# Kakao <br/><br/>

## Problem1

문제: 자물쇠와 열쇠 (https://programmers.co.kr/learn/courses/30/lessons/60059)

### Solution

Step 1. 조건 중 크게 생각할 것은 2가지이다. 
- N은 항상 M과 같거나 크다.
- 회전은 총 4번 진행한다. (90,180,270,360)

<img width="188" alt="스크린샷 2022-04-29 오후 11 30 52" src="https://user-images.githubusercontent.com/60414900/165965365-30317fce-c7c3-4f88-a613-7fb7d52f869a.png">

Step 2. 기존 자물쇠의 크기를 3배로 늘린다. 그 이유는 어차피 키가 자물쇠보다 작기 때문에 가능하다.

Step 3. 커지 자물쇠에 키 값을 비교하며 값으 바꿔주고 오리지널 자물쇠의 값이 전부 1이면 True르 return 하고 아닐 시 다이 0 으로 바꿔주는 것을 반복한다.

Step 4. 회전이 가능하기 때문에 위 Step3을 회전 시킨후 한번씩 더 반복 시켜 준다.

<br/>

## Problem2

문제: 표 편집 (https://programmers.co.kr/learn/courses/30/lessons/81303)

### Solution

Step 1. 알고리즘 자체가 너무 단순해서 시작은 리스트로 진행했다.
- 효율성에서 극한의 실패를 맛보았다.

Step 2. 연결리스트를 이용해서 진행했다. 그러기 위해서 간단하게 연결리스트르 이용해서 어떻게 풀었는지 도식화 한다.

<img width="307" alt="스크린샷 2022-04-29 오후 11 34 40" src="https://user-images.githubusercontent.com/60414900/165966034-45fac336-caaf-4e2c-badc-39a4d902a846.png">

Step 3. 리스트의 경우 삽입,삭제가 O(N)이지만 연결리스트의 경우 O(1) 이다.

<br/>

## Problem3

문제: 보석쇼핑 (https://programmers.co.kr/learn/courses/30/lessons/67258)

### Solution

Step 1. 인덱싱으로 접근하였다가 효율성 부분에서 틀렸고, 또한 예외 케이스를 계속 틀렸다.

Step 2. 잦은 검색을 이용할때는 리스트보다 Dict를 이용해야한다. (해싱을 사용하기 때문)

<img width="366" alt="스크린샷 2022-05-07 오전 1 06 44" src="https://user-images.githubusercontent.com/60414900/167170595-a9650fea-1d9e-44b0-be34-a8d21d014685.png">

Step 3. Set을 이용하여 우선 정답을 구했고 start와 end index를 사용하여 끝 값을 찾았다.

Step 4. 이후 end index를 높여가며 계속해서 보석의 갯수가 같은지 비교하였다.

Step 5. 문제의 예외케이스는 보석의 종류가 다 존재하는 구간이 2개일때 이다. 이때 만약 뒷 구간이 더 짧은 구간일때를 생각하지 못했다.

Step 6. 즉 최소 길이 구간을 저장해놓고 end index가 움직였을때 사라지면 start index를 올려주고 이것을 반복해서 끝가지 간다.


<br/>

## Problem4

문제: 불량 사용자 (https://programmers.co.kr/learn/courses/30/lessons/64064)

### Solution

Step 1. 경우의 수 문제이다.

Step 2. 처음에 중복을 제거하지 않아서 계속 오류가 생겼고 꼭 중복을 제거해 줘야 한다.

<img width="309" alt="스크린샷 2022-05-07 오전 1 09 54" src="https://user-images.githubusercontent.com/60414900/167171077-94fe12cc-82b6-4b43-bb3f-529999ac2721.png">

Step 3. 즉 불량 사용자가 될 수 있는 경우의 수를 구하는 것이기 때문에 (응모자아이디) C (불량 사용자 아이디) 중 가능한 것을 고르면 된다.

<br/>

## Problem5

문제: 합승 택시 요금 (https://programmers.co.kr/learn/courses/30/lessons/72413)

### Solution

Step 1. 플로이드-워셜 알고리즘을 이용하여 풀었다.

Step 2. S라는 노드에서 출발하여 특정노드(A or B의 집)를 거쳐서 가는 것이기 때문에 각 경로로 갈때의 최단 거리 값을 구해야 한다.

Step 3. 각 노드별로 다른 노드로 가는 최소값을 구한다. 

Step 4. 결국 s에서 시작하여 A -> B (B->A 도 결국 반대로 같은 길을 가기 때문에 동일)의 최소 값을 구한다. 
# S->A->B

<img width="223" alt="스크린샷 2022-05-23 오전 9 20 44" src="https://user-images.githubusercontent.com/60414900/169722766-cc1f4411-890c-4339-b4da-5fce7e67b865.png">



<br/>

## Problem6

문제: 경주로 건설 (https://programmers.co.kr/learn/courses/30/lessons/67259)

### Solution

Step 1. 최단거리를 구하는 문제로 bfs를 이용하여 풀었다.

Step 2. 회전에 대한 가중치만 설정해주면 된다. 직선일 경우 +100, 코너 추가시 +600 이다.

Step 3. 그렇기 때문에 직진인지 커브인지 확인하기 위한 요소를 확인해야 한다. 또한 최초의 시작에는 어떻게 해도 코너가 생기지 않는다.

Step 4. 하지만 만약에 벽인 경우도 고려하여 벽이거나 경주로 밖으로 가는 경우는 못가도록 막는다.

<img width="181" alt="스크린샷 2022-05-23 오전 9 20 53" src="https://user-images.githubusercontent.com/60414900/169722776-ef1109c8-7596-4460-8213-c2a7e3bea237.png">










