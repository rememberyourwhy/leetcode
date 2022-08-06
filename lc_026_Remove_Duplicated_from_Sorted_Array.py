#problem return length of a new array which is duplicate removed from given array
#do this with out require memory to allocate new array
#time must be liner
#memory must be constant

"""
#copy sample solution
class Remove_duplicated_from_Sorted_Array:
    def __main__(arr):
        next_new = 0
        for i in range(len(arr)):
            if i == 0 or a[i] != a[i-1]:
                arr[next_new] = num[i]
                next_new += 1
    return next_new
arr = [1, 1, 3, 4, 5, 5, 6, 6, 7, 7, 7, 7, 9]
print(Remove_duplicated_from_Sorted_Array.__main__(arr))
"""

#write solution document here

#short, clear explaination
    #this problem ask us to create no new array.
        #So we will have to change elements on place
        #solution 1 from this: check condition for both old elements and new elements
            #this solution is a dead end, we cant create a solution from this
        #solution 2 from this: we dont check the element we gonna replace
            #instead of that just replace new elements on top of it
            #the new array always append slower than the loop through old array
                #so no worry if the index of new array will exceed above the loop

        #So we go with solution 2:
            #How to do it??
                #Mentally: we have to think abt the new array is seperate array
                    #How we gonna work if we can create new array?
                        #about the elements of the array
                        #(special condition)add first element cause it not gonna be duplicated
                        #check if arr[i] != arr[i-1]
                            #if that is true, add that element to new array
                        #about length of the new array
                        #we will do the same thing
                            #check special condition than add 1 to the length
                            #check arr[i] != arr[i-1]
                                #add 1 if the condition above is true
                        #to sum both things, we will check condition
                            #first arr[new_len] = arr[i]
                            #second new_len += 1
                    #after thinking abt it as separated array
                        #we apply the same way of thinking when we have to work in one array
                        #so we gonna overwrite
                #algorithm:
                    #loop through the array (as i)
                    #check if i == 0 or arr[i] == arr[i-1]:
                        #arr[new_len] = arr[i]
                        #raise new_len

"""Second try without sample code"""

"""
class Remove_duplicated_from_Sorted_Array:
    def __main__(arr):
        new_len = 0
        for i in range(len(arr)): #loop through the array
            if i == 0 or arr[i] != arr[i-1]: #check special condition and first appear element
                arr[new_len] = arr[i] #if true assign arr[new_len] = arr[i]
                new_len += 1    #raise new_len
        return new_len          #return new_len after going through the whole array
arr = [1, 1, 3, 4, 5, 5, 6, 6, 7, 7, 7, 7, 9]
print(Remove_duplicated_from_Sorted_Array.__main__(arr))
print(arr[:7])
"""
#explain the code
    #new length = 0
        #this new_len variable is also next index variable
            #loop through the array (with i as index)
                #check if i == 0 or arr[i] != arr[i-1]
                    #do: gib the value to new_array index, in other word, new_len
                    #raise new_len
    #return new_len

#try write the code once again
class Remove_duplicated_from_Sorted_Array:
    def __main__(arr):
        new_len = 0
        for i in range(len(arr)):
            if i == 0 or arr[i] != arr[i-1]:
                arr[new_len] = arr[i]
                new_len += 1
        return new_len
arr = [1, 1, 3, 4, 5, 5, 6, 6, 7, 7, 7, 7, 9]
print(Remove_duplicated_from_Sorted_Array.__main__(arr))
print(arr[:7])


