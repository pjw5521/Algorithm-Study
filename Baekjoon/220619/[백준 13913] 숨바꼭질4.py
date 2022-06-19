from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
count = 0  # 이동 횟수를 저장할 변수
q = deque()
q.append((n, count))

max_cnt = 100001

visited = [False] * max_cnt  # 이미 방문한 적 있는 위치를 다시 반복하여 오지 않도록
visited[n] = True  # 입력받은 수빈이의 위치에 해당하는 값은 방문 처리

route = [-1] * max_cnt # 자신의 ㄱ
result = []


while q:
    curr_n, count = q.popleft() # (방문한 숫자, tree 높이)
    if curr_n == m:
        print(count)  # 첫째 줄에 이동하기까지 걸린 시간 출력
        result.append(curr_n)
        a = route[curr_n]
        print(a)
        while a != -1:
            print(a,route[a])
            result.append(a)
            a = route[a]
        result.reverse()  # 바로 출력 안된다.

        print(*result)  # 역순으로 알아서 출력해준다.
        break

    for i in (curr_n + 1, curr_n - 1, 2 * curr_n):  # 움직일 수 있는 방법 세가지를 반복
        if 0 <= i < max_cnt:
            if visited[i] == False:
                visited[i] = True
                route[i] = curr_n
                q.append((i, count + 1))
