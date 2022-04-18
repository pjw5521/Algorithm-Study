from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)
    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])
    for key in routes.keys():
        routes[key].sort(reverse=True)
    print(routes)
    stack = ['ICN']
    i = 0
    while stack:
        tmp = stack[-1]
        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())
        print(i,tmp,stack,answer)
        i+=1
    answer.reverse()
    return answer

ticket1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
ticket2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

print(solution(ticket1))