from collections import deque


def check(word, begin):
    diffs = 0
    for i in range(len(word)):
        if list(word)[i] != list(begin)[i]:
            diffs += 1
    if diffs == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    queue = deque()
    queue.append([begin, []])

    if target not in words:
        return 0

    while queue:
        n, l = queue.popleft()
        for word in words:
            if word not in l and check(word, n):
                if word == target:
                    return len(l) + 1
                temp = l[0:]
                temp.append(word)
                queue.append([word, temp])

    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
