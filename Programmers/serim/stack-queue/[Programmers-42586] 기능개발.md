## 42578 위장

Queue 자료구조 - collections.deque 모듈 / deque 자료형 사 

***

### Idea

* 큐에 각 작업에 대해 작업 일수 삽입
```
queue.append(math.ceil((100 - progresses[i]) / speeds[i]))
```

* queue에 남은 작업이 없을 때까지 수행
* popleft()를 통해 먼저 수행해야 하는 작업부터 순차적으로 수행
* 먼저 수행해야 하는 작업의 일수가 현재 작업보다 길 경우
  * 함께 수행해야 하는 작업의 개수가 1 증가
```
if first >= now:
    num += 1
```
* 먼저 수행해야 하는 작업의 일수가 현재 작업보다 짧을 경우
  * 현재 작업의 개수를 result 리스트에 추가
  * 작업의 개수 1로 초기화하고, 현재 popleft()한 작업이 가장 먼저 수행되는 작업에 대입됨
```
else:
    result.append(num)
    num = 1
    first = now
```
