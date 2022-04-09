def solution(enroll, referral, seller, amount):
    referrals = dict(zip(enroll, referral))
    profit = dict(zip(enroll, [0 for _ in range(len(enroll))]))

    for i in range(len(seller)):
        money = amount[i] * 100
        now = seller[i]
        while True:
            if money < 10:
                profit[now] += money
                break
            else:
                mine = money - money // 10
                profit[now] += mine
                if referrals[now] == "-":
                    break
                money = money // 10
                now = referrals[now]

    return list(profit.values())