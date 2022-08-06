#problem: what do we have to do?
    #we have to delete all elements that have same value (given value)
    #return the array new len

#how should we solve this problem
    #we want to avoid making a new array
    #so we will overwrite elements that needed to be delete
        #first we also use new_len variable to save new_len of the array
            #new_len is also our index
            #loop through every elements in the array
                #overwrite elements that is not required to be deleted
                #raise the pointer of the new array

#how the algorithm works:
    #first we assign 0 for new_len (so if we want to write any element
        #we have to do it first, before raise the index
    #after finishing the loop, return the new len

class Remove_Element:
    def __main__(arr, val):
        new_len = 0
        for i in range(len(arr)):
            if arr[i] != val:
                arr[new_len] = arr[i]
                new_len += 1
        return new_len

arr = [1, 1, 3, 4, 5, 5, 6, 6, 7, 7, 7, 7, 9]
print(Remove_Element.__main__(arr, 7))
print(arr[:9])
