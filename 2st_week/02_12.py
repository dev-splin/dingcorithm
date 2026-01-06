input = "abcba"


def is_palindrome(string):
    if len(string) <= 1:
        return True

    first = string[0]
    end = string[-1]

    if first == end:
        return is_palindrome(string[1:-1])
    else:
        return False


print(is_palindrome(input))