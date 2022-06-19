import math

# 소수 체크
def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False

    return True

def run(level):
    global N

    # 자리 수
    if level == N:
        # 1자리 ~ N자리 까지 소수 체크
        for i in range(N):
            temp = "".join(arr[0:i+1])

            # 1이면 return
            if int(temp) == 1:
                return
            # 소수 체크
            if is_prime_num(int(temp)):
                continue
            else:
                return

        # 저장
        result.append(temp)
        return

    # N자리 수
    for i in range(1, 10):
        arr.append(str(i))
        run(level+1)
        arr.pop()

N = int(input())
result = []
arr = []
run(0)

# 출력
for answer in result:
    print(answer)