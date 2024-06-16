# 3. Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24




def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result