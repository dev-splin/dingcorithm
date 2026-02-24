from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

# 북 동 남 서
dc = [-1, 0, 1, 0]
dr = [0, 1, 0, -1]

def move(game_map, dir, col_row):
    col, row = col_row
    new_col, new_row = col + dc[dir], row + dr[dir]

    # 한 쪽 방향으로 벽이나 구멍에 닿을 때 까지 이동
    while game_map[new_col][new_row] == ".":
        col, row = new_col, new_row
        new_col, new_row = col + dr[dir], row + dc[dir]

    return [col, row]


def solve(game_map, turn):
    if turn > 10:
        return False

    red, blue, hole = [], [], []

    # red, blue, hole 위치 저장
    for col in range(1, len(game_map) - 1):
        for row in range(len(game_map[col])):
            if game_map[col][row] == "B":
                blue = [col, row]
            elif game_map[col][row] == "R":
                red = [col, row]
            elif game_map[col][row] == "O":
                hole = [col, row]

    # 4방향 이동
    for dir in range(4):
        print("=== turn, dir ===", turn, dir)
        # blue가 구멍에 들어가는 쪽으론 기울 수 없음
        new_blue_col, new_blue_row = move(game_map, dir, blue)
        if [new_blue_col, new_blue_row] == hole:
            continue

        # red가 구멍에 들어가면 종료
        new_red_col, new_red_row = move(game_map, dir, red)
        if [new_red_col, new_red_row] == hole:
            return True

        # red/blue 이동 후 다음 턴
        game_map[new_blue_col][new_blue_row] = game_map[blue[0]][blue[1]]
        game_map[new_red_col][new_blue_row] = game_map[red[0]][red[1]]

        print(game_map)

        solve_result = solve(game_map, turn + 1)
        if solve_result:
            return True

    return False

def is_available_to_take_out_only_red_marble(game_map):
    return solve(game_map, 1)


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다



game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
["#", "#", "#", "#", "#", "#", "#"],
["#", ".", ".", "R", "#", "B", "#"],
["#", ".", "#", "#", "#", "#", "#"],
["#", ".", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", ".", "#"],
["#", "O", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))