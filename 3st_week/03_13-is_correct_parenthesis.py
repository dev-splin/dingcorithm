def is_correct_parenthesis(string):
    stack = []

    for char in string:
        if char == "(":
            stack.append(char)
            continue

        if len(stack) == 0:
            return False

        tmp = stack.pop()
        if tmp != "(":
            return False

    if stack:
        return False

    return True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))