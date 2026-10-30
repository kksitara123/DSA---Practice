
# LeetCode Problem 9: Palindrome Number
# Difficulty: Easy
# Language: Python
# Topic: Math

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        original = x
        reverse = 0

        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10

        return original == reverse
