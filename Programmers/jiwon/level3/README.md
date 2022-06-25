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
</br>

## **징검다리 건너기**

### 문제 링크
- https://programmers.co.kr/learn/courses/30/lessons/64062

### 풀이 방법 
- 우선 범위가 매우 크므로 이분 탐색으로 접근 
- 건널 수 있는 사람 수를 mid로 설정해서 이분 탐색 실행 

- 시간 초과 발생 코드 
    - 건널 수 있는 사람 수 만큼 직접 배열 값 변경해주고, 연결된 0의 개수를 세어서 가능한지 검사
    - 정확성을 통과했으나 효율성은 통과하지 못함 
    - 이분 탐색 안에 이중 for문을 수정해야겠다고 생각 
        ``` python
        import copy
        def solution(stones, k):
            answer = 0
            
            start = 1
            end = max(stones)
            
            while start <= end :
                # 건널 수 있는 최대 사람 수 
                mid = (start + end) // 2 
                tmp_s = copy.deepcopy(stones)
                check = False
                
                # 건널 수 있는 사람 수 만큼 
                for _ in range(mid) :
                    # 건너 뛸 디딤돌 칸 수 
                    cnt = 0 
                    
                    for i in range(len(stones)):
                        if tmp_s[i] == 0 :
                            cnt += 1 
                            
                            if cnt >= k :
                                check = True 
                                break 
                        else :
                            cnt = 0 
                            tmp_s[i] -= 1 
                        
                    if check :
                        break 
                    
                if check :
                    # 건널 수 있는 사람 수 줄이기 
                    end = mid -1
                else :
                    answer = mid 
                    start = mid + 1                

            return answer
        ```
- 수정한 코드 
    - 이중 for문을 아래처럼 변경하여 가능한지 검사 
    ``` python
    for s in stones :
        # 건너뛰어야 하는 디딤돌
        if s - mid <= 0 :
            cnt += 1               
        else :
            cnt = 0 
        
        if cnt >= k :
            break 
    ```
    
</br>

## **길 찾기 게임**

### 문제 링크
- https://programmers.co.kr/learn/courses/30/lessons/42892

### 풀이 과정 
- 다른 블로그 풀이 참고 

1. nodes 배열에 노드의 위치, 노드 번호 저장 
2. nodes를 y 좌표는 내림차순, x 좌표는 오름차순 정렬
- y 좌표가 가장 큰 것이 루트 노드, 그리고 차례대로 y좌표따라 내려가면서 왼쪽부터 x 좌표 기준으로 이진 노드로 채우면 됨 
3. preorder 실행 
- 중심이 될 루트 노드 기준으로 x 좌표 값 비교해서 작으면 왼쪽 트리에 추가, 크면 오른쪽 트리에 추가
- 전위 순회이므로 answer에 현재 노드 추가 -> 왼쪽 트리 순회 -> 오른쪽 트리 순회 순으로 재귀 함수 실행 
4. postorder 실행
- 중심이 될 루트 노드 기준으로 x 좌표 값 비교해서 작으면 왼쪽 트리에 추가, 크면 오른쪽 트리에 추가
- 후위 순회이므로 왼쪽 트리 순회 -> 오른쪽 트리 순회 ->  answer에 현재 노드 추가 순으로 재귀 함수 실행 

</br>

- 재귀 함수 문제로 인해 아래 코드 추가 안해주면 테스트 케이스 6,7번에 대해서 런타임 에러 
``` python
import sys
sys.setrecursionlimit(10**6)
```

</br>


## **기둥과 보 설치**

### 문제 링크
- https://programmers.co.kr/learn/courses/30/lessons/60061

### 풀이 과정 
- 구현 문제
- 문제에 제거된 조건대로 구현해주면 됨 
- 문제의 조건에 겹치게 설치되는 경우나, 없는 구조물을 삭제하는 경우는 없다고 했기 때문에 구현이 엄청 까다롭진 않았음 

</br>

설치일 때
1. 기둥일 때
    - 바닥에 있으면 기둥 설치 
    - 바닥에 있지 않으 보나 기둥 위에 있으면 기둥 설치 
2. 보일 때
    - 한쪽 끝부분이 기둥 위에 있거나, 양쪽 끝 부분이 다른 보와 동시에 연결되어 있으면 보 설치 
 
</br>

제거일 때 
1. 기둥일 때 
    - 위에 기둥이 있다면 
        - 위에 설치된 기둥이 보의 위에 있는 것이 아니면 제거하지 않음 
    - 오른쪽 위에 보가 있으면 
        - 오른쪽 위에 설치된 보의 양쪽 끝 부분이 다른 보와 연결된 게 아니고, 반대편이 기둥 위가 아니면 제거 하지 않음
    - 왼쪽 위에 보가 있으면 
        - 왼쪽 위에 설치된 보의 양쪽 끝 부분이 다른 보와 연결된 게 아니고, 반대편이 기둥 위가 아니면 제거 하지 않음
    - 위 조건에 해당하지 않으면 answer에서 제거하고, build_col에도 제거 표시  
2. 보 일 때 
    - 왼쪽 위에 기둥이 있다면 
        - 왼쪽 위에 설치된 기둥의 아래에 기둥이 없고 왼쪽에 보도 없다면 제거하지 않음 
    - 오른쪽 위에 기둥이 있다면 
        - 오른쪽 위에 설치된 기둥의 아래에 기둥이 없고 오른쪽에 보도 없다면 제거하지 않음 
    - 왼쪽에 보가 있다면   
        - 왼쪽에 설치된 보의 양쪽 아래에 기둥이 없다면 제거하지 않음 
    - 오른쪽에 보가 있다면 
        - 오른쪽에 설치된 보의 양쪽 아래에 기둥이 없다면 제거하지 않음 
    - 위 조건에 모두 해당하지 않으면 answer에거 제거하고, build_row에도 제거 표시 
    
<br/>

## **아이템 줍기**

### 문제 링크
- https://programmers.co.kr/learn/courses/30/lessons/87694

### 풀이 방법
- 문제의 핵심은 **그래프의 크기를 두 배로 늘리는 것**
    - 선으로 연결되지 않았어도(이동할 수 없는 위치라도) 두 위치 모두 그래프에 1로 표시되어 있기 때문에 bfs는 이동이 가능하다고 판단하여 발생하는 문제 제거 
1. 네모 테두리만 표시
2. bfs로 최단 거리 구하기 