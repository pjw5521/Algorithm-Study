import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())
graph  = [[] for _ in range(n + 1)]
visited = [False] * (n + 1) # 방문 체크를 위해

for _ in range(n - 1): # 자신과 붙어 있는 그래프 구하기
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)


dp = [[0, 0] for _ in range(n + 1)] # 이제 최소 값을 구하기 위해 노드 [나 o][나 x]

def solve_dp(num):
  visited[num] = True
  dp[num][0] = 0
  dp[num][1] = 1 # 자신 포함시키기(얼리어답터 수)
  for i in graph[num]:
    if not visited[i]:
      solve_dp(i)
      dp[num][0] += dp[i][1]
      dp[num][1] += min(dp[i][0], dp[i][1])



solve_dp(1)
print(min(dp[1][0], dp[1][1]))