"""
class Solution:
    def checklongerstring(s_bi1, s_bi2):
        if len(s_bi1) >= len(s_bi2):
            return s_bi1, s_bi2 #long, short
        else:
            return s_bi2, s_bi1 #long, short
    def add_binary(s_bi1, s_bi2):
        #check which string is longer and assign for specific variable
        l_str, s_str = Solution.checklongerstring(s_bi1, s_bi2)[0], Solution.checklongerstring(s_bi1, s_bi2)[1]

        s_bi_s = [0] * len(l_str)  #array that we are going to save sum of the two binary string
        left = len(l_str) - len(s_str) #find the last index when both string have value
        n = 0 #what is left unadded after the addition

        #we will cut the process into 3 parts
            #part when both have digits
            #part when only longer binary have digits but n is still left unadded somewhere
            #part when no n is left
        #the part where both string having digits
        for i in range(-1, len(l_str)- left , -1):
            s_bi_s[i] = int(l_str[i]) + int(s_str[i]) + n
            n = 0
            if s_bi_s[i] >= 2:
                s_bi_s[i] -= 2
                n = 1
        #the part where only l_string is left:
        if len(l_str) == len(s_str) and n == 1:
            return [1] + s_bi_s
        i = left - 1
        while n == 1 and i >= 0:
            s_bi_s[i] += 1
            n = 0
            if s_bi_s[i] >= 2:
                s_bi_s[i] -= 2
                n = 1
            i -= 1
        if i < left - 1:
            i += 1
        if i == 0 :
            return [1] + s_bi_s
        else:
        #the part where we just simply copy value from l_str
            s_bi_s[:i + 1] = l_str[:i + 1]
            return s_bi_s

s_bi1 = "101"
s_bi2 = "1100"
print(Solution.add_binary(s_bi1, s_bi2))
"""
#Above
#Totally too complicated
#everything is unclear
#just do another one which is clearer

#first appoach: extend the short string so we can add them easily
    #without branched programming
"""
class Solution:
    def compare_change(b1, b2):
        if len(b1) >= len(b2):
            long = b1
            short = b2
        else:
            long = b2
            short = b1
        left = len(long) - len(short)
        short = "0" * left + short
        return long, short
    def add_binary1(b1, b2):
        c_c = Solution.compare_change(b1, b2)
        long, short = c_c[0], c_c[1]
        result = ""
        n = 0
        for i in range(len(long)-1, -1, -1):
            temp = int(long[i]) + int(short[i]) + n
            n = 0
            if temp >= 2:
                temp -= 2
                n = 1
            result = str(temp) + result
        if n == 1:
            result = "1" + result
        return result

b1 = "101"
b2 = "101"
added_bi = Solution.add_binary1(b1, b2)
print(added_bi)
"""
#second approach:
    #not much different from first one but, ok
    #we will no longer add extened part to the short string
    #we instead use branched programming
    #if index >= -len(short) we do add the short string.
    #elif index =< -len(short) and n != 0:
        #add long[index] + n
    #elif index =< -len(short) and n = 0:
        #result = long[len(long)- index:] + result
"""
class Solution:
    def temp_to_result(temp, result):
        n = 0
        if temp >= 2:
            temp -= 2
            n = 1
        result = str(temp) + result
        return temp, n, result
    def add_binary2(b1, b2):
        #check long and short
        if len(b1) >= len(b2):
            long = b1
            short = b2
        else:
            short = b1
            long = b2
        n = 0
        result = ""
        for index in range(-1, -len(long), -1):
            #if index is not exceeeded the range of short string
            if index >= -len(short):
                temp = int(long[index]) + int(short[index]) + n
                n = 0
                #use temp check to check value, return updated temp and n
                temp_n_result = Solution.temp_to_result(temp, result)
                temp, n, result = temp_n_result[0], temp_n_result[1], temp_n_result[2]
            #when it exceeded the range of short string but n is still left
            elif index < -len(short) and n != 0:
                temp = int(long[index]) + n    
                temp_n_result = Solution.temp_to_result(temp, result)
                temp, n, result = temp_n_result[0], temp_n_result[1], temp_n_result[2]
            #when index exceeded the range of short array and n == 0
            elif index < -len(short) and n == 0:
                result = long[index] + result
        if n == 1:
            result = "1" + result
            return result
b1 = "101"
b2 = "1111101"
add_bi = Solution.add_binary2(b1, b2)
print(add_bi)
"""

#the right, clear approach:
    #use two pointers for this
    #one pointer for string1 and another for string2
    #we will run down the string
        #check if the pointer of each is >= 0 or not
            #add that to total
            #append that total value mod 2 to the array
            #get total div 2 for carry

class Solution:
    def add_binary3(a, b):
        i = len(a) - 1
        j = len(b) - 1
        result = []
        carry = 0
        while carry or i >= 0 or j >= 0:

            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2

        return "".join(result[::-1])
b1 = "101"
b2 = "1111101"
result = Solution.add_binary3(b1, b2)
print(result)