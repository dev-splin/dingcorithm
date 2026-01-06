def factorial(n):
    if n > 1:
        return factorial(n - 1) * n
    
    return 1


print(factorial(5))