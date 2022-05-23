# 플로이드와샬, 다익스트라 알고리즘

def solution(n, s, a, b, fares):
    inf = 1e9
    answer = inf

    cost_map = [[inf]*(n+1) for _ in range(n+1)]
    for i,j,cst in fares:
        cost_map[i][j] = cost_map[j][i] = cst
        # 위아래 대칭 행렬이므로
    for i in range(1,n+1):
        cost_map[i][i] = 0
        # 자기가 자기자신한테 가는건 0

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if cost_map[i][j] > cost_map[i][k] + cost_map[k][j]:
                    cost_map[i][j] = cost_map[i][k] + cost_map[k][j]
    print(cost_map)
    for i in range(1,n+1):
        cost = cost_map[s][i] + cost_map[i][a] + cost_map[i][b]
        print(a,b)
        answer = min(answer,cost)
    return answer

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

n1 = 7
s1 = 3
a1 = 4
b1 = 1
fares1 = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

n2 = 6
s2 = 4
a2 = 5
b2 = 6
fares2 = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]

print(solution(n,s,a,b,fares))

#print(solution(n1,s1,a1,b1,fares1))

#print(solution(n2,s2,a2,b2,fares2))

