finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array):
    array.sort()

    min = 0
    max = len(array) - 1

    while min <= max:
        curIndex = (min + max) // 2
        curNum = array[curIndex]
        print(curNum, target)
        if curNum == target:
            return True
        elif curNum < target:
            min = curIndex + 1
        elif curNum > target:
            max = curIndex - 1

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)