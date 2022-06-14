# 재귀 방식의 dfs

def dfs(num):
    # 수의 제곱근까지 나누었는데 나누어지는 수가 없을 경우 => 소수
    for i in range(2, int(int(num) ** 0.5) + 1):
        # 나누었을 때 나머지가 0이 되는 수가 존재할 경우 소수가 아니므로 반환
        if int(num) % i == 0:
            return

    # 길이 n이 되면 출력
    if len(num) == n:
        print(num)
        return

    # 숫자 자릿수를 하나씩 늘려가며 재귀를 통해 소수 검사
    # 자릿수가 늘어났을 때 일의 자리가 '2,4,6,8,0'인 수는 2로 무조건  나누어지고 '5'인 수는 5로 무조건 나누어진다.
    for j in '1379':
        dfs(num + j)

n = int(input())

# 자릿수가 1일때 소수가 되는 수는 2, 3, 5, 7
for k in '2357':
    dfs(k)