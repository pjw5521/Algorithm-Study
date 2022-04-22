# https://bladejun.tistory.com/43

def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[0], reverse=True)
    print(routes)

    now = routes[0][0]
    #print(routes[1:])
    for i in routes[1:]:
        #print(i)
        if i[1] >= now:
            print(i[1])
            continue
        else:
            now = i[0]
            print(i[1],now)
            answer += 1

    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

routes2 = [[-20,-13],[-16,-4],[-14,-10],[-10,-5],[-3,-1]]
print(solution(routes))