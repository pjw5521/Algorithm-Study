import math


def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance
    answer = 0
    while left <= right:
        prev = 0
        mins = math.inf
        removed_rocks = 0

        mid = (left + right) // 2
        for i in range(len(rocks)):
            if rocks[i] - prev < mid:
                if i != len(rocks) - 1:
                    removed_rocks += 1
            else:
                mins = min(mins, rocks[i] - prev)
                prev = rocks[i]

        if removed_rocks > n:
            right = mid - 1
        else:
            answer = mins
            left = mid + 1
    return answer
