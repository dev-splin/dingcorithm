input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count = [0,0]

    prev = string[0]
    for char in string:
        if char != prev:
            count[int(prev)] += 1
            prev = char

    result = min(count[0], count[1])
    if result == 0:
        result = 1

    return result


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)