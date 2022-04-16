answer = 99999999

def dfs(words, visited, begin, target, cnt):
    global answer

    # 변환 과정이 answer보다 크면
    if answer < cnt:
        return

    # 찾았을 때
    if begin == target:
        answer = cnt
        return

    for i in range(len(words)):
        # 다른 알파벳 수
        count = 0
        for k in range(len(begin)):
            if begin[k] != words[i][k]:
                count += 1

        # 한 개의 알파벳이 다를 때
        if count == 1:
            # 사용하지 않은 단어
            if visited[i] == 0:
                visited[i] = 1
                dfs(words, visited, words[i], target, cnt + 1)
                visited[i] = 0


def solution(begin, target, words):
    global answer
    visited = [0] * len(words)

    # words에 target이 없으면
    if target not in words:
        answer = 0
    # words에 target이 있을 때
    else:
        dfs(words, visited, begin, target, 0)

    return answer
