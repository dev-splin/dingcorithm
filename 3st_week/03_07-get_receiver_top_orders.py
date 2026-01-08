top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    result = []
    index_stack = []

    for i in range(len(heights)):
        while len(index_stack) > 0 and heights[index_stack[-1]] < heights[i]:
            index_stack.pop()

        if len(index_stack) == 0:
            result.append(0)
        else:
            result.append(index_stack[-1] + 1)

        index_stack.append(i)

    return result


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 2, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))