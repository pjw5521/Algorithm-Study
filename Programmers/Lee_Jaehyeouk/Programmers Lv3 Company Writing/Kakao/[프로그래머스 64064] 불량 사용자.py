from itertools import permutations

def compare(user, ban):
    if len(user) != len(ban):
        return False
    else:
        for i, j in zip(user, ban):
            if j == '*':
                continue
            if i != j:
                return False
        return True


def solution(user_id, banned_id):
    answer = []

    # 경우의 수를 생각 했을 때 조합으로 생각한다.
    for i in permutations(user_id, len(banned_id)):
        count = 0
        # 가능한 경우의 수인지 체크 하기 위하 카운트
        for a, b in zip(i, banned_id):
            print(i,a,b)
            if compare(a, b):
                count += 1
                # 체크 성공시 카운트 추가
        if count == len(banned_id):
            # 중복을 제거한다. 예시 5C2에서 5*4/2*1 인 경우 밑에 부분에 해당한다고 생각하면 된다.
            if set(i) not in answer:
                answer.append(set(i))
    return len(answer)

u1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b1 = ["fr*d*", "abc1**"]

u2 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b2 = ["*rodo", "*rodo", "******"]
u3 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b3 = ["fr*d*", "*rodo", "******", "******"]


print(solution(u1,b1))


