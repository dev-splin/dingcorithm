def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue

        alphabet_occurrence_array[ord(char) - ord('a')] += 1

    maxIndex = 0;
    maxCount = 0;
    for i, count  in enumerate(alphabet_occurrence_array):
        if count <= maxCount:
            continue

        maxCount = count
        maxIndex = i

    return chr(maxIndex + ord('a'))
ㅁ

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))