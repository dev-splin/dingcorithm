from main import print_hi

numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    if len(array) > 0:
        newArray = array.copy()
        num = newArray.pop()
        return get_count_of_ways_to_target_by_doing_plus_or_minus(newArray, target + num) + get_count_of_ways_to_target_by_doing_plus_or_minus(newArray, target - num)

    if target == 0:        return 1
    else:
        return 0


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!