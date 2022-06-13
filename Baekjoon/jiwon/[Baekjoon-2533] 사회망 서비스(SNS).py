# https://www.acmicpc.net/problem/2533
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline 

def dfs(n):
    visited[n] = True 
    dp[n][0] = 1 
    
    for i in graph[n]:
        if not visited[i] :
            dfs(i)
            # n이 얼리아답터이면 자식 노드가 얼리아답터 상관 x -> 작은 값 가져오기 
            dp[n][0] += min(dp[i][0], dp[i][1])
            # n이 얼리아답터가 아니면 자식은 무조건 얼리아답터여야 함 
            dp[n][1] += dp[i][0]
            
n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# dp[i][0] : i번 노드가 얼리아답터가 아닐 때 최소 수
# dp[i][1] : i번 노드가 얼리아답터 일 때 최소 수 
dp = [ [0,0] for _ in range(n+1) ]
visited = [False] * (n+1)

# 어디를 시작점으로 잡아도 상관없음 
dfs(1)
# 더 작은 경우 출력 
print(min(dp[1][0], dp[1][1]))