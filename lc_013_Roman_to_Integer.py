#There are some rules in roman number
    #bigger number on the left
    #there are single numbers and double numbers
        #Doubles: CM = 900, CD = 400, XC = 90, XL = 40, IX = 9, IV = 4
        #Singles: M = 1000, D = 500, C = 100, L = 50, X = 10, V = 5, I = 1

#Problem: return integer number from a given roman number

#Solution:
    #use dictionary to store key, value of the doubles and singles seperatedly
    #check if there is a double number next or single number next than sum them up in a variable

class Solution:
    def roman_to_integer(roman):
        doubles = {'CM' : 900, 'CD' : 400, 'XC' : 90, 'XL' : 40, 'IX' : 9, 'IV' : 4}
        singles = {'M' : 1000, 'D': 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}
        i = 0
        s = roman
        integer = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i + 2] in doubles:
                integer += doubles[s[i: i + 2]]
                i += 2
            else:
                integer += singles[s[i]]
                i += 1
        return integer

roman = "MCM"
print(Solution.roman_to_integer("MCM"))
print(Solution.roman_to_integer("XIX"))