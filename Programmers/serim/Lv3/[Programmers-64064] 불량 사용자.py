from itertools import permutations

def compare(user, banned_id):
    for i in range(len(banned_id)):
        if len(user[i]) != len(banned_id[i]):
            return False
        for j in range(len(user[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != user[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    user_combi = list(permutations(user_id, len(banned_id)))
    case = []

    for user in user_combi:
        if not compare(user, banned_id):
            continue
        else:
            user = set(user)
            if user not in case:
                case.append(user)
    return len(case)