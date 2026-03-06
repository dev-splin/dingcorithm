import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]

def get_min_city_chicken_distance(n, m, city_map):
    homes = []
    chickens = []
    # 집,치킨집 찾기
    for row_index in range(n):
        for col_index in range(n):
            if city_map[row_index][col_index] == 1:
                homes.append((row_index, col_index))
            elif city_map[row_index][col_index] == 2:
                chickens.append((row_index, col_index))

    chicken_combis = list(itertools.combinations(chickens, m))

    min_result = sys.maxsize
    while chicken_combis:
        distance_sum = 0
        chicken_combi = list(chicken_combis.pop())

        for home in homes:
            home_row, home_col = home
            min_chicken_distance = sys.maxsize

            for chicken in chicken_combi:
                chicken_row, chicken_col = chicken
                chicken_distance = abs(home_row - chicken_row) + abs(home_col - chicken_col)
                min_chicken_distance = min(min_chicken_distance, chicken_distance)

            distance_sum += min_chicken_distance

        min_result = min(distance_sum, min_result)

    return min_result


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!


city_map = [
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0]
]
print("정답 = 11 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,1,city_map))


city_map = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2]
]
print("정답 = 10 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,2,city_map))