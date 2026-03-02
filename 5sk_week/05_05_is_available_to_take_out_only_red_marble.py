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

def move(game_map, dir, row, col):
    count = 0
    new_row, new_col = row + dr[dir], col + dc[dir]

    # 한 쪽 방향으로 벽이나 구멍에 닿을 때 까지 이동
    while game_map[new_row][new_col] != "#" and game_map[row][col] != "O":
        count += 1
        row, col = new_row, new_col
        new_row, new_col = new_row + dr[dir], new_col + dc[dir]

    return [row, col, count]

def is_available_to_take_out_only_red_marble(game_map):
    n,m = len(game_map), len(game_map[0])
    visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]

    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
    for row in range(n):
        for col in range(m):
            if game_map[row][col] == "R":
                red_row, red_col = row, col
            elif game_map[row][col] == "B":
                blue_row, blue_col = row, col

    queue = deque()
    queue.append((red_row, red_col, blue_row, blue_col, 1))
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        red_row, red_col, blue_row, blue_col, turn = queue.popleft()
        if turn > 10:
            break

        for dir in range(4):
            # blue가 구멍에 들어가는 쪽으론 기울 수 없음
            new_blue_row, new_blue_col, blue_count = move(game_map, dir, blue_row, blue_col)
            if game_map[new_blue_row][new_blue_col] == "O":
                continue

            # red가 구멍에 들어가면 종료
            new_red_row, new_red_col, red_count = move(game_map, dir, red_row, red_col)
            if game_map[new_red_row][new_red_col] == "O":
                return True

            # red, blue가 같은 위치인 경우 조금 움직인 구슬이 자리를 차지
            if new_red_col == new_blue_col and new_red_row == new_blue_row:
                if red_count > blue_count:
                    new_red_col, new_red_row = new_red_col - dc[dir], new_red_row - dr[dir]
                else:
                    new_blue_col, new_blue_row = new_blue_col - dc[dir], new_blue_row - dr[dir]

            if not visited[new_red_row][new_red_col][new_blue_row][new_blue_col]:
                visited[new_red_row][new_red_col][new_blue_row][new_blue_col] = True
                queue.append((new_red_row, new_red_col, new_blue_row, new_blue_col, turn + 1))

    return False


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