#  DP <br/><br/>

## Problem1

정수 삼각형: https://programmers.co.kr/learn/courses/30/lessons/43105

### Solution

![스크린샷 2022-04-08 오후 6 19 55](https://user-images.githubusercontent.com/60414900/162406233-3893e4be-d705-4270-bdee-8ae0bfce81e1.png)


Step 1. 우선 위와 같은 형식의 삼각형이 있을때 공 배열 dp를 같은 크기의 배열을 생성한다.

Step 2. 위 삼각형에 노란 표시를 보면 값을 더할때 선택이 불가능하다. 왜냐하면 일반적으로 인덱스 [i-1] 혹은 [j-1] 중 max 값을 더해야하는데 그 값이 없기 때문이다.

Step 3. 위 삼각형에 분홍색 표시일때는 이전 dp라는 리스트에 저장해둔 값을 비교하여 값이 큰것을 자기와 더해서 dp에 다시 저장한다.

Step 4. 맨 마지막 dp에 있는 값 중 최대 값을 반환한다.

<br/><br/>

## Problem2   

등굣길: https://programmers.co.kr/learn/courses/30/lessons/42898

### Solution

<img width="310" alt="스크린샷 2022-04-15 오전 3 13 31" src="https://user-images.githubusercontent.com/60414900/163451748-08c396e5-8c52-4843-b12b-57da2fce4b28.png">

Step 1. 중학교 때 배우는 최단경로 경우의 수를 구하는 방법을 이용했다. 

Step 2. 문제의 조건을 잘 생각해야한다,
- [1,0], [0,1] 이 웅덩이로 막힌 경우가 존재 한다.
- puddles 가 반대로 들어온다.

<br/><br/>


## Problem3  

도둑질: https://programmers.co.kr/learn/courses/30/lessons/42897

### Solution

Step 1. 인접한 집을 방문할 경우 경보가 울리기 때문에 방문할 현재 집과 그 전전집의 합을 그 전집과 비교해야 한다. 
- dp[i] = dp[i-1], money[i]+ dp[i-2]

Step 2. 또한 케이스를 잘 나누어야 하는것은 첫번째 집으 방문하면 마지막 집은 절대로 방문하지 못한다. 그렇기 때문에 첫번째 집의 방문 여부가 중요하다.

<img width="268" alt="스크린샷 2022-04-15 오전 3 12 34" src="https://user-images.githubusercontent.com/60414900/163451811-a9cf29e3-c74b-47b7-ad17-caa5c5bb62f3.png">                      

Ex)[1,3,10,1,1,60,0] 그려보기  

<img width="575" alt="스크린샷 2022-04-15 오전 3 23 42" src="https://user-images.githubusercontent.com/60414900/163453991-dbc0f299-c908-453e-ae64-4520d3e245c3.png">

