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








