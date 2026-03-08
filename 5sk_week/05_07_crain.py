def solution(board, moves):
    n = len(board)
    convert_board = [[] for i in range(n)]
    # 각 열에 있는 데이터들을 새로운 2차원 배열의 행으로 변환
    for i in range(n):
        for j in range(n-1, -1, -1):
            if board[j][i] != 0:
                convert_board[i].append(board[j][i])

    answer = 0
    basket = []
    # moves를 순회하며 바구니에 담음
    for move in moves:
        index = move - 1
        # 데이터가 없음(빈칸)이면 스킵
        if (len(convert_board[index]) == 0):
            continue

        doll = convert_board[index].pop()
        basket.append(doll)
        # 2개 이상이면 이전 데이터와 비교
        if (len(basket) >= 2 and basket[-1] == basket[-2]):
            answer += 2
            basket.pop()
            basket.pop()

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]));