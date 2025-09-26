

def recursionwithmulty(number):
    if number == 0:
        return 1
    return number * recursionwithmulty(number-1)

print(recursionwithmulty(6))


def reverseString(s):
    if len(s)== 0:

        return s
    result = reverseString(s[1:]) + s[0]
    print(result)
    return result

print(reverseString("jitendra"))









# from typing import final
#
#
# def factorial(n):
#     if n == 0:
#         return 1
#
#     return n * factorial(n-1)
#
# print(factorial(2))
#
#
#
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#
#     return fibonacci(n-1) +fibonacci(n-2)
#
# print(fibonacci(10))
#
#
# def sum_of_digits(n):
#     if n == 0:
#         return 0
#
#     return n % 10 + sum_of_digits(n//10)
#
# print(sum_of_digits(12345))
#
# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     return reverse_string(s[1:]) + s[0]
#
#
# print(reverse_string("abscd"))
#
