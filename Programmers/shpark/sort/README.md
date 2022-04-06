## 42747 H-index

sort사용

***

##### 해결책
1. H-index의 최대값을 초기 answer에 넣어줌 -> 모든 논문이 인용 됬을 때
2. citations를 내림차순으로 sort
3. citations[i]가 i+1보다 작으면 i를 answer에 넣어줌

***

https://programmers.co.kr/learn/courses/30/lessons/42747