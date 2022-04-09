import heapq


# inser 하면 Heap 에 숫자 삽입 heappush
# d 1  큐에서 최대값을 삭제 nlargest
# d -1 큐에서 최솟값을 삭제 heappop

def solution(operations):
    answer = []
    for i in operations:
        a,b = i.split()
        if a == "I":
            heapq.heappush(answer,int(b))
        else:
            if len(answer) > 0: # 빈큐에 데이터를 삭제하는 연산이 들어왔을 때
                if b == "1":
                    answer.pop(answer.index(heapq.nlargest(1,answer)[0])) # 최소 heap에서 최대값 삭제 연산
                else:
                    heapq.heappop(answer)
    if len(answer) == 0:
        answer=[0,0]
    return [heapq.nlargest(1,answer)[0],answer[0]]

op1 = ["I 16","D 1"]
op2 = ["I 7","I 5","I -5","D -1"]

print(solution(op1))
print(solution(op2))

