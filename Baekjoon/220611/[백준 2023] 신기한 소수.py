def find(num):
    for i in range(2, int(int(num) ** 0.5) + 1):
        if int(num) % i == 0:
            return
    # 소수 판별

    if len(num) == n:
        print(num)
        return

    # 내가 지정하는 자릿수가 나오면 출력

    for p in prime:
        find(num + p)

    # 하나씩 자릿수를 더하면서 recursive

n = int(input())
start = ["2","3","5","7"]
prime = ["1","3","7","9"]
for s in start:
    find(s)