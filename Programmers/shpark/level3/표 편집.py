from collections import defaultdict
def solution(n, k, cmd):
    answer = ''
    stack = []
    dict = defaultdict()

    dict[0] = [n-1, 1]
    for i in range(1, n-1):
        dict[i] = [i-1, i+1]
    dict[n-1] = [n-2, 0]

    cur = k

    for command in cmd:
        if command[0] == 'U':
            dir, move = command.split()
            for i in range(int(move)):
                cur = dict[cur][0]
        elif command[0] == 'D':
            dir, move = command.split()
            for i in range(int(move)):
                cur = dict[cur][1]

        elif command[0] == 'C':
            stack.append([cur, dict[cur]])
            left, right = dict[cur]
            dict[left][1] = right
            dict[right][0] = left
            temp = dict[cur]
            del dict[cur]

            if temp[1] == 0:
                cur = temp[0]
            else:
                cur = temp[1]

        elif command[0] == 'Z':
            cur_node, val = stack.pop()
            left, right = val
            dict[cur_node] = [left, right]
            dict[left][1] = cur_node
            dict[right][0] = cur_node


    for i in range(n):
        if i in dict:
            answer += 'O'
        else:
            answer += 'X'

    return answer