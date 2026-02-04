input = "abcabcabcabcdededededede"


def string_compression(string):
    result = 2000

    for i in range (1, len(string) + 1):
        tmp_string = string
        count = 0
        prev = ""
        tmp_result = ""

        while tmp_string:
            split_string = tmp_string[0:i]
            tmp_string = tmp_string[i:]

            if split_string == prev:
                count += 1
            elif split_string != prev:
                tmp_result += str(count) + prev if count > 1 else prev
                prev = split_string
                count = 1

        tmp_result += str(count) + prev if count > 1 else prev

        result = min(len(tmp_result), result)

    return result


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))