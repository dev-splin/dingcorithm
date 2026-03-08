def solution(board, moves):
    answer = 0
    basket = []
    # moves를 순회하며 바구니에 담음
    for move in moves:
        index = move - 1

        # 해당 열(move)에 인형을 넣고 같은 번호가 겹치면 제거(+ answer 값 추가)
        for row in board:
            if row[index] == 0:
                continue

            basket.append(row[index])
            row[index] = 0
            # 2개 이상이면 이전 데이터와 비교
            if len(basket) >= 2 and basket[-1] == basket[-2]:
                answer += 2
                basket = basket[:-2]

            break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]));