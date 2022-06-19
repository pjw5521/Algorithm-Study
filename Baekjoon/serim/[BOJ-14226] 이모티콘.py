from collections import deque

def bfs(s):
    queue = deque()
    queue.append((1, 0))
    emoji = [[0] * (s + 1) for _ in range(s + 1)]
    emoji[1][0] = 0
    while queue:
        display, clip = queue.popleft()
        if display == s:
            print(emoji[display][clip])
            break
        # 1. 화면에 있는 이모티콘 모두 복사해서 클립보드에 저장한다.
        if emoji[display][display] == 0:
            emoji[display][display] = emoji[display][clip] + 1
            queue.append((display, display))
        # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
        if display + clip <= s and emoji[display + clip][clip] == 0:
            emoji[display + clip][clip] = emoji[display][clip] + 1
            queue.append((display + clip, clip))
        # 3. 화면에 있는 이모티콘 중 하나를 삭제한다.
        if display - 1 >= 0 and emoji[display - 1][clip] == 0:
            emoji[display - 1][clip] = emoji[display][clip] + 1
            queue.append((display - 1, clip))


s = int(input())
bfs(s)