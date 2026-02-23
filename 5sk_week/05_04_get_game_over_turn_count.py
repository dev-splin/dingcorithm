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

def in_range(n, col, row):
    return 0 <= col < n and 0 <= row < n

def set_horse_seq(seq_dic, horse_num, col, row):
    if (col, row) in seq_dic:
        seq_dic[(col, row)].append(horse_num)
    else:
        seq_dic[(col, row)] = [horse_num]

def reverse_dir(dir):
    return dir + 1 if dir % 2 == 0 else dir - 1

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    turn = 1
    seq_dic = {} # 순서 리스트 딕셔너리(key: 행렬)®
    n = len(horse_location_and_directions)

    for i in range(horse_count):
        col, row, dir = horse_location_and_directions[i]
        set_horse_seq(seq_dic, i, col, row)

    while turn <= 1000:
        for i in range(horse_count):
            col, row, dir = horse_location_and_directions[i]
            new_col, new_row, new_dir = col + dc[dir], row + dr[dir], dir

            if not in_range(n, new_col, new_row) or game_map[new_col][new_row] == 2:
                # 범위 바깥을 넘어가거나 파란색
                new_dir = reverse_dir(new_dir)
                new_col, new_row = col + dc[new_dir], row + dr[new_dir]
                horse_location_and_directions[i][2] = new_dir

                # 바꾼 방향도 파란색인 경우
                if not in_range(n, new_col, new_row) or game_map[new_col][new_row] == 2:
                    continue

            index = seq_dic[(col, row)].index(i)
            move_list = seq_dic[(col, row)][index:]
            seq_dic[(col, row)] = seq_dic[(col, row)][:index]

            if game_map[new_col][new_row] == 1:
                move_list.reverse()

            for move_horse_num in move_list:
                set_horse_seq(seq_dic, move_horse_num, new_col, new_row)
                # 행/렬/방향 기록
                horse_location_and_directions[move_horse_num][0], horse_location_and_directions[move_horse_num][1] = new_col, new_row

            # 결과 확인
            for dic in seq_dic:
                if len(seq_dic[dic]) >= EXIT_COUNT:
                    return turn

        turn += 1

    return -1


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