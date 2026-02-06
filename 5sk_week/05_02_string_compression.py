input = "abcabcabcabcdededededede"


def string_compression(string):
    n = len(string)
    result = n

    for split_size in range (1, n // 2 + 1):
        split_strings = [
            string[i:i+split_size ] for i in range(0, n, split_size)
        ]
        count = 1
        tmp_result = ""

        for i in range(len(split_strings) - 1):
            cur, next = split_strings[i], split_strings[i+1]

            if cur == next:
                count += 1
            else:
                tmp_result += f"{count}{cur}" if count > 1 else cur
                count = 1

        tmp_result += f"{count}{split_strings[-1]}" if count > 1 else split_strings[-1]

        result = min(len(tmp_result), result)

    return result


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))