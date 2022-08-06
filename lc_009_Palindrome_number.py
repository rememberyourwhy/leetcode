import timeit
#Solution 1
    #do the mod 10 div 10 approach
    #check if reversed number = given number

#Solution 2
    #turn to string and check from both side
        #assign left and right
        #loop (condition left < right)
            #check if left != right to return false
        #if loop is finished and not return yet, return True for the palindrome number
class Palindrome_number:
    def Solution_1(x):
        result = 0
        xc = x
        while xc != 0:
            result = result * 10 + xc % 10
            xc //= 10
        if result == x:
            return True
        return False
    def Solution_2(x):
        x_str = str(x)
        left, right = 0, len(x_str) - 1
        while left < right:
            if x_str[left] != x_str[right]:
                return False
            left += 1
            right -= 1
        return True

command1 = 'Palindrome_number.Solution_1(x)'
command2 = 'Palindrome_number.Solution_2(x)'
init = 'from lc_009_Palindrome_number import Palindrome_number; x = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001'
print(timeit.timeit(command1, init, number = 10000))
print(timeit.timeit(command2, init, number = 10000))
