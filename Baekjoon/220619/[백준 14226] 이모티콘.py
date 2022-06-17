from collections import deque

n = int(input())
dp = [[0 for _ in range(2001)] for _ in range(2001)]
q = deque()
q.append([1, 0, 0])
while q:
    screen, clip, time = q.popleft()
    if screen == n:
        print(time)
        break
    if dp[screen][clip]:
        continue
    dp[screen][clip] = 1
    if screen >= 1:
        q.append([screen-1, clip, time+1])
        q.append([screen, screen, time+1])
    if clip:
        q.append([screen+clip, clip, time+1])