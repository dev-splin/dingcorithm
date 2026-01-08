array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    newArray = []
    i = 0
    j = 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            newArray.append(array1[i])
            i += 1
        else:
            newArray.append(array2[j])
            j += 1

    while i < len(array1):
        newArray.append(array1[i])
        i += 1

    while j < len(array2):
        newArray.append(array2[j])
        j += 1

    return newArray


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))