seat_count = 9
vip_seat_array = [4, 7]

memo = {
    1: 1,
    2: 1
}
def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    sum = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = sum
    return sum

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    split_nums = []

    count = 0
    for num in range(1, total_count + 1):
        if num not in fixed_seat_array:
            count += 1
        elif num in fixed_seat_array:
            split_nums.append(count)
            count = 0

    if count != 0:
        split_nums.append(count)

    result = 1
    for num in split_nums:
        multiple_num = fibo_dynamic_programming(num + 1, memo)
        result *= multiple_num

    return result


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))