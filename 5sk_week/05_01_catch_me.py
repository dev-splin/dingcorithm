from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    seconds = 0
    queue = deque()
    queue.append(brown_loc)
    MAX = 200000

    while cony_loc <= MAX:
        next_brown_loc_arr = deque()
        while queue:
            cur_brown_loc = queue.popleft()
            if cur_brown_loc == cony_loc:
                return seconds
            else:
                next_brown_loc_arr.append(cur_brown_loc)

        while next_brown_loc_arr:
            next_brown_loc = next_brown_loc_arr.popleft()

            if next_brown_loc - 1 >= 0:
                queue.append(next_brown_loc - 1)
            if next_brown_loc + 1 <= MAX:
                queue.append(next_brown_loc + 1)
            if next_brown_loc * 2 <= MAX:
                queue.append(next_brown_loc * 2)

        seconds += 1
        cony_loc += seconds

    # 구현해보세요!
    return seconds


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))