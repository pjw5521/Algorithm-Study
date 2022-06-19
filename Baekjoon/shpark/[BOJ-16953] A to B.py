from collections import deque

def dfs(A, cnt):
    global answer
    if A >= int(10e9):
        return

    if A > B:
        return

    if A == B:
        if cnt < answer:
            answer = cnt
        return

    dfs(2*A, cnt+1)
    dfs(int(str(A) + '1'), cnt+1)

def bfs(A, B):
    q = deque()
    Dict = dict()
    q.append([A, 1])

    while q:
        number, cnt = q.popleft()

        for i in range(2):
            if i == 0:
                Num = number * 2
            else:
                Num = int(str(number) + '1')

            if Num >= int(10e9):
                continue
            if Num > B:
                continue
            if Num in Dict:
                continue

            q.append([Num, cnt+1])
            Dict[A] = 0
            if Num == B:
                return cnt

    return -1




A, B = map(int, input().split())

# DFS
answer = int(10e9)
dfs(A, 0)
if answer == int(10e9):
    print(-1)
else:
    print(answer + 1)


"""
# BFS
answer = bfs(A, B)
if answer == -1:
    print(-1)
else:
    print(answer + 1)
"""