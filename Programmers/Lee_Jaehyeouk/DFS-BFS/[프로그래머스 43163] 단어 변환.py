
def solution(begin, target, words):
    ans = 0
    tmp = [begin]
    visited = [0 for _ in words]

    if target not in words:
        return 0

    while tmp:
        stack = tmp.pop()
        if stack == target:
            return ans
        for i in range(len(words)):
            cnt = 0
            for j in range(len(words[i])):
                if words[i][j] != stack[j]:
                    cnt += 1
            if cnt == 1:
                if visited[i] == 1:
                    continue
                else:
                    visited[i] = 1
                tmp.append(words[i])
        ans += 1
    return ans

begin1 = "hit"
target1 = "cog"
words1 = ["hot", "dot", "dog", "lot", "log", "cog"]
words2 = ["hot", "dot", "dog", "lot", "log"]