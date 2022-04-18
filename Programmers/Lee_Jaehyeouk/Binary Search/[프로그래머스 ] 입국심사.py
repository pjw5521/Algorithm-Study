
n = 9
times = [7,10,11]
answer = []

# 7 10 11 14 20 21 22 28 30 33 35 40 42 44

for i in times:
    for j in range(1,n+1):
        answer.append(i*j)
answer.sort()
print(answer[n-1])



