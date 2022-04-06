## 43238 입국심사

이분탐색

***

##### 해결책
1. left = 1, right = 걸릴 시간의 최대값
2. mid값과 times를 이용해 심사한 사람 수 구함
3. 심사한 사람 수가 n보다 많으면 right = mid -1 , 심사한 사람 수가 n보다 적으면 left = mid + 1
4. 심사한 사람 수가 n이고 더 이상 범위를 좁힐 수 없을 때 answer return

***

https://programmers.co.kr/learn/courses/30/lessons/43238