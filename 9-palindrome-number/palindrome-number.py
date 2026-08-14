class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Numbers ending in 0 cannot be palindromes
        # unless the number itself is 0
        if x != 0 and x % 10 == 0:
            return False

        reversed_half = 0

        # Reverse only half of the number
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10

        # Even number of digits: x == reversed_half
        # Odd number of digits: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10