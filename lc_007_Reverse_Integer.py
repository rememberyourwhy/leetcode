"""
class Solution:
    def reverse(self, num):
        if num in range(-10,10):
            return num
        result = 0
        if num < 0:
            negative = True
        else:
            negative = False
        x = num
        while x != 0:
            result = result * 10 + x % 10
            x //= 10
        if negative == True:
            return result * -1
        else:
            return result

s1 = Solution()

print(Solution.reverse(s1, 1000))
"""
