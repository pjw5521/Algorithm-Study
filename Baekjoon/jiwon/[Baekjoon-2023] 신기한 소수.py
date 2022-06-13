# https://www.acmicpc.net/problem/2023
import math 

# 에라토스테네스의 채로 소수 판별 
def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False
    return True
    
# 한자릿수씩 늘려가면서 소수인지 판별 
def dfs(num):
    # n자리 수면 출력 
    if len(str(num)) == n :
        print(num)
    else :
        for i in range(10):
            # 10을 곱하고 0부터 9까지 더한 숫자  
            tmp = num*10 + i
            # 소수이면 dfs 
            if is_prime_num(tmp) :
                dfs(tmp)

n = int(input())

# 시작 숫자 
start = [2,3,5,7]

for i in start:
    dfs(i)
