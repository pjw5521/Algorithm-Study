##  다리를 지나는 트럭<br/><br/>

### Problem 
https://programmers.co.kr/learn/courses/30/lessons/42583

### Solution

Step 1. 다리가 가용할 수 있는 트럭 갯수 만큼의 크기의 zero 배열(다리) 을 만들었습니다.<br/><br/>

Step 2. while 문을 이용했고 다리가 공배열이 될 경우 종료되도록 조건을 설정했습니다.<br/><br/>

Step 3. 트럭 배열에 트럭이 존재한다면 먼저 나올 트럭과 다리 내에 있는 트럭의 무게의 합을 구해 다리의 가용 무게와 비교했습니다.
- Step 3-1) 합이 가용무게 보다 작으면 다리위에 트럭을 pop 해서 append 합니다. <br/><br/>
- Step 3-2) 합이 가용무게 보다 크다면 다리에 0을 append 해서 트럭이 한칸 전진 한것 처럼 합니다.<br/><br/>

### Algorithm flow 
<img width="618" alt="스크린샷 2022-04-03 오후 2 26 39" src="https://user-images.githubusercontent.com/60414900/161413147-43932a1e-e124-4533-9f45-8f48e48566f5.png">
<br/><br/>

### Refactoing

- 파이썬의 리스트를 Queue 와 같은 용도로 진행했습니다. 















