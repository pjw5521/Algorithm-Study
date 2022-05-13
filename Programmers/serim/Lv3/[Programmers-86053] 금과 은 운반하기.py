def solution(a, b, g, s, w, t):
    answer = int(10 ** 16)
    start, end = 0, int(10 ** 16)

    while start <= end:

        mid = (start + end) // 2
        gold = 0
        silver = 0
        total = 0

        for i in range(len(g)):
            cnt = mid // (t[i] * 2)
            if mid % (t[i] * 2) >= t[i]:
                cnt += 1
            if w[i] * cnt <= g[i]:
                gold += w[i] * cnt
            else:
                gold += g[i]
            if w[i] * cnt <= s[i]:
                silver += w[i] * cnt
            else:
                silver += s[i]
            if s[i] + g[i] >= w[i] * cnt:
                total += w[i] * cnt
            else:
                total += s[i] + g[i]

        if gold >= a and silver >= b and total >= a + b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1

    return answer