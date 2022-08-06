
#Solution 1
    #special condition:
        #two sum/ 2 appear two time in our arr

    #turn list to set,
        #get the needed_add number than search in set
            #return True if there is one
        #return False after the loop finished
"""
class Solution:
    def two_sum(arr, target):
        if Solution.special_condition(arr, target)[0]:
            return Solution.special_condition(arr, target)[1]
        if Solution.normal_condition(arr, target)[0]:
            return Solution.normal_condition(arr, target)[1]
        return False
    def special_condition(arr, target):
        count = 0
        i = 0
        special_num = target / 2
        while count < 2 and i < len(arr):
            if i == special_num:
                count += 1
            i += 1
        if count == 2:
            return (True, [special_num, special_num])
        return (False, None)
    def normal_condition(arr, target):
        set_arr = set(arr)
        for i in set_arr:
            needed_add = target - i
            if needed_add in set_arr:
                return (True, [i , needed_add])
        return (False, None)
arr = [6, 6, 14, 53, 65, 20, 1]
target = 12
print(Solution.two_sum(arr, target))
"""

#Solution 2: use dictionary

    #Short explaination
        #store key value as num, time_appear
        #run through key in dict
            #try except if needed_add is available or not
                #If yes return two keys (numbers)

    #Long explaination
        #__main__
            #turn to dict. key, value = num, time appeared
            #check special condition, than do normal condition an get return value of it
                #if there is any value satisfy our problem, return key, needed_add

            #special condition
                #check double value that sum is target

            #normal condition
                #run through the dict
                    #run check_add function get return value
                        #if True return satisfied values
                        #False, pass
                    #check add:
                        #check if needed_add = target- key is in dict
                        #return both values, and True
                #if finished the run but still no value satisfy problem return false
"""
class two_sum_dict:
    def __main__(arr, target):
        dict = two_sum_dict.get_dict(arr) #jump to get dict -> get a dict in return
        if two_sum_dict.special_condition(dict, target)[0] == True: #jump to special condition
            return two_sum_dict.special_condition(dict, target)[1] #return key, needed_add of special condition
        if two_sum_dict.two_sum_check(dict, target)[0] == True: #jump to normal condition (two sum check in dict)
            return two_sum_dict.two_sum_check(dict, target)[1] #return key, needed_add
        return False
    def get_dict(arr):
        dict = {}
        for i in arr: #run through arr
            if i in dict: #check if i alr in dict -> raise value
                dict[i] += 1
            else: #if not appeared yet -> set value to 1
                dict[i] = 1
        return dict
    def check_add(dict, target, key): #return True if there is any satisficed key in dict.
        needed_add = target - key
        if needed_add in dict:
            return (True, [key, needed_add])
        return (False, None)
    def two_sum_check(dict, target):
        for key in dict: #run through key in dict
            check = two_sum_dict.check_add(dict, target, key) #assign return values of chekc_add to check
            if check[0] == True: #if there is any check_add is True return this function
                return check
        return (False, None) #if finished the loop but still no -> return False
    def special_condition(dict, target): #check special condition if there is a number that is doubled in arr satisfy two sum
        special_double = int(target / 2)
        if special_double in dict:
            if dict[special_double] >= 2:
                return (True, [special_double, special_double])
            else:
                return (False, None)
        return (False, None)
arr = [6, 6, 14, 53, 65, 20, 1]
target = 67
print(two_sum_dict.__main__(arr, target))

"""
#Simple solution :
    #move through the list, add it to a dictionary
    #also check if the target- element is in the list yet or not
    #return both value if found

#declare the dict
#loop through
    #check target - element in the dictionary
    #add the element into the dictionary

#what exactly the algorhithm we are using here?
    #instead of 2 pointer loop, we use only one pointer
    #but this problem asking us to check the other values in the list as well
    #so we save it up in a dictionary to check later, dictionary check is O(1) so
        #our problem from O(n^2) become O(n)

class Solution:
    def two_sum(arr, target):
        ind_of_num = {}
        for i in range(len(arr)):
            if target - arr[i] in ind_of_num:
                return ind_of_num[target- arr[i]], i
            ind_of_num[arr[i]] = i
        return -1

arr = [1, 3, 5]
target = 8
result = Solution.two_sum(arr, target)
print(result)

#what does the program actually do
#LOOP starts
#first i check index 0
    #it checked if target - arr[i] which is 8 - 1 is there yet
        #no, so that condition did get executed
    #it store that value and its index into the dictionary
        #[1 : 0]

#now i check the index 1:
    # it checked if target- arr[i] which is 8- 3 is in the dictionary
        #False -> the condition didnt get execute.
    #store the value and its index into the dicitonary
        #[3: 1]

#index 2:
    #check if target - arr[i] is alr there
        #3, so 3 is in keys.[ind_of_num]
            #the condition command will get execute
                #return values of dict key [8 - 5] = 3 -> 1, index of this i, 2

class Solution:
    def two_sum(arr, target):
        #declare the dictionary
        num_index = {}
        for i in range(len(arr)):
            if target - arr[i] in num_index:
                return num_index[target- arr[i]], i
            num_index[arr[i]] = i
        return -1

target = 10
arr= [1, 3, 5, 2, 7]
result = Solution.two_sum(arr, target)
print(result)