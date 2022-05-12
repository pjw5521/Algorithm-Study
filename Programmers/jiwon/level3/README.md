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

</br>

## **합승 택시 요금**

### 문제 링크
- https://programmers.co.kr/learn/courses/30/lessons/72413

### 풀이 방법
- n의 크기가 최대 200이므로 플로이드 워셜로 모든 정점에서부터 다른 정점까지의 최단 거리를 구해줌 
- 출발 지점에서부터 다른 지점까지 함께 갔다가 도착 지점까지 가는 거리들을 비교해가며 최소 비용 구하기 
- 한 지점까지 가는 경우만 체크해도 되는 이유는 어차피 최단 거리로 갈 것이기 때문에 경로는 정해져 있음 

## **광고 삽입**

### 문제 링크
- https://programmers.co.kr/learn/courses/30/lessons/72414

### 풀이 방법
- 처음엔 logs를 끝나는 시간 기준으로 정렬 후 다음 동영상의 시작 시간이 전 동영상의 end 시간보다 빠르다면 구간에 포함된 동영상의 시청자 수를 +1 해주는 방식으로 접근했으나, 구현 실패  
- 다른 사람의 풀이를 참고하니 전혀 생각하지 못했던 dp 문제 
- dp로 구간별 누적 시청자 수를 구하고 최댓값 갱신해줘야 함 

1. 전체 시간, 광고 시간 초 단위로 통일 
2. 모든 로그들에 대해 시작 시간과 종료 시간을 초 단위로 변경 후, result[start]는 +1, result[end] -1 
    - result[i]는 i 시각에 시청 중인 사람의 수
    - start 에서는 누군가 시청을 시작했으므로 +1 , end 에서는 누군가 시청을 종료했으므로 -1 
    - 즉, 시작과 끝만 표시해주는 것 
3. 구간 별 시청자 수 기록 
    - 2번에서 시작과 끝 시청자 수를 기록했으므로, 누적합을 통해 구간 별 시청자 수를 기록
    ```python
    result[i] = result[i-1] + result[i]
    ```
4. 모든 구간의 누적 시청자 수 기록
    - 3번에서 구간 별 시청자 수를 기록했으므로, 누적합을 통해 누적 시청자 수를 구한다.
    - result[i]는 0초부터 i초까지의 누적 시청자 수 
    ```python
    result[i] = result[i-1] + result[i]
    ```
5. 누적된 시청자 수를 바탕으로, 가장 시청자 수가 많은 부분을 탐색한다. 
    ```python
    view = result[i] - result[i-adv_time]
    ```