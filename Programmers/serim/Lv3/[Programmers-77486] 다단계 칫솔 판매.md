# 77486 다단계 칫솔 판매

*Hash 구현 - 딕셔너리 자료형 사용*

##문제 풀이

- referrals ⇒ enroll과 referral은 크기가 같은 리스트. zip을 이용하여 key가 조직원, value가 추천인인 딕셔너리 생성
- profit ⇒ key : 조직원, value : 수익
- seller와 amount를 돌면서 하나씩 profit에 값을 추가해준다.
- 이익금이 10원 이하라면 모든 이익금이 판매자에게로 돌아간다
    
    ```python
    if money < 10:
        profit[now] += money
        break
    ```
    
- 그렇지 않으면, 
**현재 판매자의 추천인 = 이익금 // 10
현재 판매자 = 이익금 - 이익금 // 10**
을 얻게된다.
    
    ```python
    else:
        mine = money - money // 10
        profit[now] += mine
        if referrals[now] == "-":
            break
        money = money // 10
        now = referrals[now]
    ```
    
    - 만약 추천인이 민호일 경우 반복문을 중단하고 다음 seller로 넘어간다
    - 그렇지 않을 경우, money에 추천을 통해 받은 이익금을 젖아하고, now에 추천인을 저장하여 부모 노드에 대해 같은 작업을 반복한다.