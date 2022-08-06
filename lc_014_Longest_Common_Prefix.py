#first we will sort the string elements
#then compare first and last string since they will share the biggest difference

#code like explaination:
    #special condition: if not s_list: return '' (list of array is none, return '')
    #sort() to sort the array
        #assign left and right for first and last string
    #set i = 0
    #in a while loop:
        #condition: i < len(left) and i < len(right) and left[i] == right[i]:
        #i += 1
    #return the substring from index [0] to index [i]

#explain the code:
    #check special condition when the given list is empty
    #sort the list
        #to get first index string and last index string be the most difference
    #assign left, right, i as first, last, 0
    #in a while loop raise i for each element alike in both strings
    #return the prefix string
"""
class longest_common_prefix:
    def __main__(s_list):
        #check special condition
        if not s_list:
            return ''
        #do normal condition, sort the list
        sorted(s_list)
        #assign left, right, i
        left, right, i = s_list[0], s_list[-1], 0
        #in a while loop check condition, raise i
        while i < len(left) and i < len(right) and left[i] == right[i]:
            i += 1
        return left[:i]
"""

#explaination:
    #check special condition
    #sort list, assign left, right elements
    #i = 0
    #in a while loop check condition i< len(left) & len(right) and left[i] == right[i]
    #return substring from first index to i (last index when left[i] == right[i])

# a quick second try
class longest_common_prefix:
    def __main__(s_list):
        if not s_list:
            return ''
        sorted(s_list)
        left, right, i = s_list[0], s_list[-1], 0
        while i < len(left) and i < len(right) and left[i] == right[i]:
            i += 1
        return left[:i]

s_list = ["flower","flow","flight"]
print(longest_common_prefix.__main__(s_list))
