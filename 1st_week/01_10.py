input = "abadabac"

def find_not_repeating_first_character(string):
    count = [0] * 26
    for char in string:
        index = ord(char) - ord("a")
        count[index] += 1

    result = "_"
    for char in string:
        index = ord(char) - ord("a")
        if (count[index] == 1):
            result = char
            break;
            
    return result


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))