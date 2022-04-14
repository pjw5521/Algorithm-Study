def solution(N, number):
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(int(a / b))
        if number in dp[i]:
            return i
    return -1


def solution2(N, number):
    answer = -1
    dp = []

    for i in range(1, 9):
        all_case = set()
        check_number = int(str(N) * i)
        all_case.add(check_number)
        for j in range(0, i - 1):
            for op1 in dp[j]:
                for op2 in dp[-j - 1]:
                    all_case.add(op1 - op2)
                    all_case.add(op1 + op2)
                    all_case.add(op1 * op2)
                    if op2 != 0:
                        all_case.add(op1 // op2)

        if number in all_case:
            answer = i
            break
        dp.append(all_case)
    return answer


N = 5
numbers = 12
print(solution2(5,12))
