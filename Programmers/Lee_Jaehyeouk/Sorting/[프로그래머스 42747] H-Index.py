def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        if len(citations[i:]) >= i:
            answer = i
            print(answer)
    return answer

# 리펙토링 여기서 이해할 것은 l-i 가 무엇인지
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i: # 이부분이 바로 H번 이상 인용된 논문이 h편 이상인 것 3
            return l-i
    return 0

x = [6,6,6,6,6,1]
c = [3,0,6,1,5]
d = [8,8,8,8,8,8,8,8,8,8,8]
print(solution(x))
# answer =  3


