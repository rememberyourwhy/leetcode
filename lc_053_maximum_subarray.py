#first approach
class Solution:
    def maximum_subarray_1(arr): #O(n^3)
        m_sum = arr[0]
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                c_sum = 0 #after get first and last index of the subarray, reset current_sum
                for k in range(i, j + 1): #loop through subarray, add arr[k] to current_sum
                    c_sum += arr[k]
                    m_sum = max(m_sum, c_sum) #compare with max_sum
        return m_sum
    def maximum_subarray_2(arr): #O(n^2)
        m_sum = arr[0] #assign m_sum = arr[0]
        for i in range(len(arr)): #loop through every index of the array
                                    #this one is the first index of each subarray
            c_sum = arr[i] #reset current sum as arr[i] so we can reduce one index loop each first index
            m_sum = max(m_sum, c_sum) #compare, update max_value
            for j in range(i + 1, len(arr)): #loop from i + 1 index to the end of the array, since we alr compare and execute the subarray contain only i
                c_sum += arr[j] #raise current_sum
                m_sum = max(m_sum, c_sum) #compare new current_sum with max_sum then update max_sum
        return m_sum
    def maximum_subarray_3(arr): #Time: O(n)
        m_sum = arr[0]
        c_sum = 0
        for i in arr:
            c_sum += i
            m_sum = max(m_sum, c_sum) #why do this first, cause if we reset c_sum first
                                        #we will easily run into error when max = 0 and
                                            #every element in the array is negative
            if c_sum < 0:
                c_sum = 0
        return m_sum
arr = [-1, 3, -2, 5, 2, -4]
arr2 = [-3, -5, -9, -29, -2, -4]
print(Solution.maximum_subarray_1(arr))
print(Solution.maximum_subarray_2(arr))
print(Solution.maximum_subarray_3(arr))
print(Solution.maximum_subarray_3(arr2))

#3 level of this problem
#level 1: time O(n^3)
    #i = loop through whole array find left index of subarray
        #j = loop from i to the end of the array to find right index of the subarray
            #k = loop from i to j (left index to right index) to add every element of the subarr
                #to current_sum
                #compare max_sum and current sum then update max_sum
#level 2: time O(n^2)
    #i = loop through whole array
        #reset current_sum = arr[i]
        #j loop from i + 1 to the end of the array (we alr do exe.arr[i])
            #update current_sum by add one more element to it
            #compare and update max_sum
                #compare:               (with current_sum)
    #level 1 and level 2 share the same following traits:
        #check every subarray of the array

#level 3: time: O(n):
    #if c_sum < 0 it will only ruin later c_sum.
        #so when c_sum < 0 we will reset it
        #result: our new subarray wont get ruin by that and we also dont have to check for it
    #in the end\



