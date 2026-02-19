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

def in_range(horse_location_and_directions, col, row):
    col_length = len(horse_location_and_directions)
    row_length = len(horse_location_and_directions[0])

    return 0 <= col < col_length and 0 <= row < row_length

def remove_horse_seq(seq_dic, horse_num, col, row):
    index = seq_dic[(col, row)].index(horse_num)
    seq_dic[(col, row)].pop(index)

def set_horse_seq(seq_dic, horse_num, col, row):
    if (col, row) in seq_dic:
        seq_dic[(col, row)].append(horse_num)
    else:
        seq_dic[(col, row)] = [horse_num]

def move(game_map, horse_location_and_directions, seq_dic, horse_num):
    col, row, pos = horse_location_and_directions[horse_num]
    next_col, next_row, new_pos = col + dc[horse_num], row + dr[horse_num], pos

    index = seq_dic[(col, row)].index(horse_num)
    move_list = seq_dic[(col, row)][index:]

    if not in_range(horse_location_and_directions, next_col, next_row) or game_map[next_col][next_row] == 2:
        # 범위 바깥을 넘어가거나 파란색
        next_col, next_row = col - dc[horse_num], row - dr[horse_num]
        new_pos = pos + 1 if pos == 0 or pos == 3 else pos - 1
    elif in_range(horse_location_and_directions, next_col, next_row) and game_map[next_col][next_row] == 1:
        # 범위 내이면서 빨간색
        move_list.reverse()

    for move_horse_num in move_list:
        # 기존 순서 리스트에서 데이터 제거 후 다음 순서 리스트에 기록
        remove_horse_seq(seq_dic, move_horse_num, col, row)
        set_horse_seq(seq_dic, move_horse_num, next_col, next_row)
        # 행/렬/위치 기록
        horse_location_and_directions[move_horse_num] = [next_col, next_row, new_pos]

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    turn = 0
    seq_dic = {} # 순서 리스트 딕셔너리(key: 행렬)®

    for i in range(horse_count):
        [col, row, _] = horse_location_and_directions[i]
        set_horse_seq(seq_dic, i, col, row)

    while turn <= 1000:
        # 결과 확인
        for dic in seq_dic:
            if len(seq_dic[dic]) >= EXIT_COUNT:
                return turn

        # 이동 처리
        for i in range(horse_count):
            move(game_map, horse_location_and_directions, seq_dic, i)

        turn += 1

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