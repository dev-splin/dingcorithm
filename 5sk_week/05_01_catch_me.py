from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    MAX = 200000
    seconds = 0
    queue = deque()
    queue.append(brown_loc)
    visited = [{} for _ in range(200001)]

    while cony_loc <= MAX:
        cony_loc += seconds

        if seconds in visited[cony_loc]:
            return seconds

        for i in range(len(queue)):
            cur_brown_loc = queue.popleft()
            if cur_brown_loc == cony_loc:
                return seconds

            next_seconds = seconds + 1
            next_brown_loc = cur_brown_loc - 1
            if 0 <= next_brown_loc <= MAX and next_seconds not in visited[next_brown_loc]:
                queue.append(next_brown_loc)
                visited[next_brown_loc][next_seconds] = True

            next_brown_loc = cur_brown_loc + 1
            if 0 <= next_brown_loc <= MAX and next_seconds not in visited[next_brown_loc]:
                queue.append(next_brown_loc)
                visited[next_brown_loc][next_seconds] = True

            next_brown_loc = cur_brown_loc * 2
            if 0 <= next_brown_loc <= MAX and next_seconds not in visited[next_brown_loc]:
                queue.append(next_brown_loc)
                visited[next_brown_loc][next_seconds] = True

        seconds += 1


    # 구현해보세요!
    return seconds


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))