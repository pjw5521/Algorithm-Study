##  정수 삼각형 <br/><br/>

### Problem  
https://programmers.co.kr/learn/courses/30/lessons/43105  

### Solution

![스크린샷 2022-04-08 오후 6 19 55](https://user-images.githubusercontent.com/60414900/162406233-3893e4be-d705-4270-bdee-8ae0bfce81e1.png)


Step 1. 우선 위와 같은 형식의 삼각형이 있을때 공 배열 dp를 같은 크기의 배열을 생성한다.

Step 2. 위 삼각형에 노란 표시를 보면 값을 더할때 선택이 불가능하다. 왜냐하면 일반적으로 인덱스 [i-1] 혹은 [j-1] 중 max 값을 더해야하는데 그 값이 없기 때문이다.

Step 3. 위 삼각형에 분홍색 표시일때는 이전 dp라는 리스트에 저장해둔 값을 비교하여 값이 큰것을 자기와 더해서 dp에 다시 저장한다.

Step 4. 맨 마지막 dp에 있는 값 중 최대 값을 반환한다.
