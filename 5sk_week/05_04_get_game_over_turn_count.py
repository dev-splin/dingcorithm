k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# 0 행, 1 열, 2 방향
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]

MAX_TURN = 1000
EXIT_COUNT = 4

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):

    col_length = len(horse_location_and_directions)
    row_length = len(horse_location_and_directions[0])
    turn = 0
    seq_dic = {}

    while turn <= 1000:
        # 순서 등록
        for i in range(horse_count):
             col, row, pos = horse_location_and_directions[i]

            if (col, row) in seq_dic:
                seq_dic[(col, row)].append(i)
            else:
                seq_dic[(col, row)] = [i]

        # 결과 확인
        for dic in seq_dic:
            if len(seq_dic[dic]) >= EXIT_COUNT:
                return turn

        # 이동 처리
        for i in range(horse_count):
            col, row, pos = horse_location_and_directions[i]
            next_col, next_row = col + dc[i], row + dr[i]

            if 0 <= next_col < col_length and 0 <= next_row < row_length:

                # # 흰색
                # if game_map[next_col][next_row] == 0:
                #     horse_location_and_directions[i] = [next_col, next_row, pos]
                # # 빨간색
                # elif game_map[next_col][next_row] == 1:








    return -1 if turn > 1000 else turn


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다

start_horse_location_and_directions = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
print("정답 = 9 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

start_horse_location_and_directions = [
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0],
    [2, 1, 2]
]
print("정답 = 3 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))