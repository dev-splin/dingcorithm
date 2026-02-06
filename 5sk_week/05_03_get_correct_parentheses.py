from collections import deque

balanced_parentheses_string = "()))((()"


def get_correct_parentheses(balanced_parentheses_string):
    # 1
    if not balanced_parentheses_string:
        return ""

    left_queue = deque()
    right_queue = deque()
    u, v = "", ""
    # 2
    for i in range(len(balanced_parentheses_string)):
        string = balanced_parentheses_string[i]
        if string == "(":
            left_queue.append(string)
        elif string == ")":
            right_queue.append(string)

        if len(left_queue) == len(right_queue):
            u = balanced_parentheses_string[0:i+1]
            v = balanced_parentheses_string[i+1:]
            break

    # 3,4번 판단
    stack = []
    isCorrect = True
    for i in range(len(u)):
        string = u[i]
        if string == "(":
             stack.append(string)
        elif string == ")":
            if stack:
                stack.pop()
            else:
                isCorrect = False
                break

    if stack:
        isCorrect = False






    return


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))