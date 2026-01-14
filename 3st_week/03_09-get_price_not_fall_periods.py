from collections import deque

prices = [1, 2, 3, 2, 3]


def get_price_not_fall_periods(prices):
    queue = deque(prices)
    result = []

    while queue:
        cur_num = queue.popleft()
        seconds = 0

        for num in queue:
            seconds += 1
            if num < cur_num:
                break

        result.append(seconds)

    # 이 부분을 채워주세요!
    return result


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))