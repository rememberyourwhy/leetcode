#first, store value in a dict and a list
    #what is in the dictionary:
        #key, value: '(' : ')', '[', ']', '{', '}'
        #a new list store parentheses that is working right now
            #not closed parentheses
    #run i throughout the string:
        #check if i is open parentheses or close parentheses
            #if open parentheses add str[i] into the list
            #if close parentheses check if list_parentheses.pop() != str[i]:
                #if the condition is true return false for the function

class valid_parentheses:
    def __main__(pare_str):
        #make dictionary store open and close parentheses
        dict_pa = {'(' : ')', '[' : ']', '{' : '}'}
        #create new list
        l_pa = []
        #check special condition
        if pare_str[0] in dict_pa.values():
            return False
        if pare_str == '':
            return True
        #loop through every elements and check
        for element in pare_str: #run through the pare_str
            if element in dict_pa.keys(): #check if element is open parentheses.
                l_pa.append(element)        #If true add that to the list
            elif dict_pa[l_pa.pop(-1)] != element: #if not open than it gonna be close parentheses.
        #use dict pop to get the first parentheses must be closed. l_pa.pop(). return an open parenthese
        #use that open parenthese as a key to return its value dict_pa[l_pa.pop(-1)] return a close parenthese
        #if that close parenthese is not the element we are suspecting then this string is false
                return False
        #one thing to notice here is we dont use pop again to check cause we alr pop an element and if the condition is true we can skip else:
            #which im doing here
        return l_pa == []
        #after finish the loop if l_pa is empty, mean that we popped all elements and didnt find any error


pare_str = '}(())[]{()}'
print(valid_parentheses.__main__(pare_str))


#explain my code
    #first i will store 3 pairs of parentheses in an dictionary
    #then i create a new empty list to store only open parentheses.
        #why there is no close parentheses in my list,
            #because if a close parenthese is true. that parenthese will be passed
            #if it is wrong close parenthese, the whole function will return False
    #check special condition when the
    #loop through every elements in the string:
        #check if it is an open parenthese. append that open parenthese to our list
        #if it is a close parenthese, check if it is right close
            #if true, pass
            #if false, return False for the whole function
