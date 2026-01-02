# BOJ 1158

def josephus_problem(n, k):
   result = []
   arr = list(range(1,n + 1))

   nextIndex = k - 1
   while arr:
       num = arr.pop(nextIndex)
       result.append(num)
       if len(arr) != 0:
           nextIndex = (nextIndex + k - 1) % len(arr)

   print("<",", ".join(map(str, result)),">", sep='')

n, k = map(int, input().split())
josephus_problem(n, k)