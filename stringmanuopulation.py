#
#
# a = "abcdefghijkl"
# print(a.replace("f", ''))
# from collections import Counter
def is_validPalindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1   
        right -=1
    return True


def validPalindrome(s):
    left = 0
    right = len(s) -1
    while left < right:
        if s[left] != s[right]:
            return is_validPalindrome(s, left+1, right) or is_validPalindrome(s, left, right-1)
        left += 1
        right -= 1
    return True

print(validPalindrome("abca"))