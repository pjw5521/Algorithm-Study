# 백준 1주차 <br/><br/>

## Problem1

문제: 신기한 소수 (https://www.acmicpc.net/problem/2023)

### Solution

Step 1. 첫째 자리 소수의 경우는 2,3,5,7 이며 그 이상 자릿수의 소수는 뒤에 1,3,7,9 외에는 올 수 없다.

Step 2. 해당 규칙을 이용하여 dfs를 이용해서 풀었다.

<br/>

## Problem2

문제: 두 동전 (https://www.acmicpc.net/problem/16197)

### Solution

Step 1. bfs 최단 시간 알고리즘을 이용했다.

Step 2. bfs에서 두 동전 좌표를 인자로 받는다.

Step 3. 함수를 시작하며 체크를 위해 두 동전의 위치 파악을 위한 4차원 배열을 만든다.

Step 4. 두 동전의 첫 위치를 0으로 표시하고 큐에 담는다.

Step 5. 큐에 값이 있는 동안 하나씩 꺼내며 bfs를 실시한다. 
- 이때 10번 이상이면 실패이므로 -1 을 return

Step 6.고려해줄 경우는 다음과 같다.
- 두 동전 모두 이동할 위치가 격자 밖이면 continue
- 위에서 걸러지므로 둘 중 한 동전만 격자 밖이면 현재 위치값 + 1한 값을 리턴한다.
- 이동할 곳이 벽이면 이동하지 않으므로 원 위치 시킨다.
- 이동할 곳이 첫 방문일 경우에만 새 위치에 현 위치 + 1한 값으로 표시하고 큐에 담는다.


<br/>

## Problem3

문제: ACM Craft (https://www.acmicpc.net/problem/1005)

### Solution

Step 1. 위상 정렬과 dp 를 이용하여 풀었다.

Step 2. 시간 테이블과 dp 테이블을 각각 만든다.

Step 3. 처음 진입 차수가 0인 노드를 queue에 넣을때, 그 노드들의 자리에 시간을 담는다. 

Step 4. queue 를 순회하며 위상정렬을 시행한다. q에서 꺼낼 때마다 그 노드를 부모로 갖고 있는 노드들의 진입차수를 1 감소시키는 것은 일반적인 위상정렬과 동일하다. 이 때, dp테이블에 부모dp와 현 노드가 걸리는 시간을 더해야한다. 부모 노드가 여러 개 일경우에는 큰 시간이 답이므로 max함수를 사용하였다.

Step 5. 진입 차수가 0이 되면 queue에 넣고 반복한다.

<img width="315" alt="스크린샷 2022-06-14 오후 7 54 43" src="https://user-images.githubusercontent.com/60414900/173561490-b7fb12c0-68b0-4144-993e-dd1de1fdf3c7.png">


<br/>

## Problem4

문제: 사회망 서비스(SNS) (https://www.acmicpc.net/problem/2533)

### Solution

Step 1. 트리 dp 문제이다.

Step 2. dp[num][1]: 정점 번호가 index이고 자신이 얼리 어답터인 경우에는 자식 노드가 얼리 어받터일때와 아닐때를 구분해서 그 중 작은 값을 더한다.

```python
    dp[num][1] += min(dp[i][0], dp[i][1])
```


Step 3. dp[num][0]: 정점 번호가 index이고 자신이 얼리 어답터가 아닌 경우에는 자식 노드가 무조건 얼리 어답터여야 하기 때문에 dp[i][1]을 더해준다. 

```python
    dp[num][0] += dp[i][0]
```

<img width="329" alt="스크린샷 2022-06-14 오후 7 54 26" src="https://user-images.githubusercontent.com/60414900/173561445-193fed85-b481-46a4-91e9-ba7b84830301.png">






