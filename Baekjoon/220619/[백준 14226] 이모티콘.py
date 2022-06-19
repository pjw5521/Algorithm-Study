from collections import deque

n = int(input())
visited = [[0 for _ in range(2001)] for _ in range(2001)]
q = deque()
q.append([1, 0, 0])
while q:
    screen, clip, time = q.popleft()
    print(screen,clip,time)

    if screen == n: # 화면 내 이모티콘이 내가 원하는 값에 도달했으니 return
        print(time)
        break

    if visited[screen][clip]: # 방문기록 o 인경우
        continue

    visited[screen][clip] = 1 # 방문기록이 x인 경우

    if screen >= 1:
        q.append([screen-1, clip, time+1])
        q.append([screen, screen, time+1])
    if clip:
        q.append([screen+clip, clip, time+1])