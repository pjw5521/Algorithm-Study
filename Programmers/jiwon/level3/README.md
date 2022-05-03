# 문제 풀이

## **보석쇼핑**

### 문제링크
-  https://programmers.co.kr/learn/courses/30/lessons/67258

### 풀이 방법 
1. 처음 접근 방식 : 효율성을 고려하지 않은 단순 반복문, set()으로 구현
```python
def solution(gems):
    answer = []
    n = len(gems)
    # 서로 다른 보석의 개수 
    num = len(set(gems))
    # 최소 구간 거리 
    length = n 
    
    for i in range(n):
        s = set()
        s.add(gems[i])
        for j in range(i,n):
        	# 최소 구간 거리보다 길면 중단 
            if j-i >= length:
                break 
            s.add(gems[j])
            # 구간에 모든 보석이 존재한다면 
            if len(s) == num:
            	# 정답 추가 
                answer.append((j-i, i+1,j+1))
                # 최소 구간 거리 갱신 
                length = j-i
                break
    
    # 구간 거리 기준으로 정렬 
    answer.sort()
    
    # 가장 짧은 거 
    return [answer[0][1], answer[0][2]]
```
- 예상대로 효율성 통과 불가 

2. 투포인터 
- 완전 탐색의 경우, 시간 초과가 발생할 때 투포인터를 고려할 수 있다. 
- 그러나 이 방법 역시 정확성은 모두 통과했으나, 효율성을 전혀 통과하지 못함 
```python
# 시간 초과 발생 코드 
def solution(gems):
    answer = []
    g_num = len(set(gems))
    start = 0
    end = 0
    
    answer = [0, len(gems)-1]
    while start <= end  and end < len(gems) :
        # 범위 안에 보석들이 다 있으면 
        if len(set(gems[start:end+1])) == g_num:
            # 더 짧은 구간으로 갱신 
            if end - start < answer[1] - answer[0]: 
                answer = [start, end]
            start += 1
        else :
            end += 1 
            
    answer[0] += 1 
    answer[1] += 1 
    return answer
```

3. defaultdict을 사용한 투포인터 
- 보석 이름을 key, 구간에 포함된 개수를 value로 하여 value 값이 1보다 더 클 때 범위를 좁혀주는 방식 


</br>


## **2 x n 타일링**

### 문제링크
-  https://programmers.co.kr/learn/courses/30/lessons/12900

### 풀이 방법
- dp 문제 
- dp[i] = dp[i-1] + dp[i-2] 라는 점화식을 도출할 수 있다. 
    - dp[i-1]에서 세로 막대기 하나 놓을 때 
    - dp[i-2]에서 가로 막대기 두개 놓을 때  
    
</br>


## **불량 사용자**

### 문제 링크
- https://programmers.co.kr/learn/courses/30/lessons/64064

### 풀이 방법 
- user_id 배열의 크기가 최대 8이므로 순열로 모든 경우의 수 구해서 가능한지 확인 
- 가능하다면 set으로 변경하여 순서와 관계없이 아이디 목록의 내용이 동일하면 같은 것으로 처리 