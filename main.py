#1
# Biggie Size: a function that will change all positive numbers to “big”
#input = a list of numbers (positive and negative) \ output = a list with “big” instead of positive integers 
# use a for loop to go through each element in the list and then an if statement to check if the number is positive  


def biggie_size(lst):
    for i in range(len(lst)):
        if lst[i] > 0: 
            lst[i] = "big"
    return lst
print (biggie_size([-2,-5,2,5]))

#2
# Count positive: a function that will replace the last item in the list with the number of positive values in the list 
#input = a list of -\+ numbers \ output: the same list but the last element is the number of positive values
# use a for loop that goes over every item in the list and an if statement to check if the item is positive
#create a variable that = 0 and will increase every time the function finds a + number 
#then replace the last value in the list with the count 
\
def count_positives(lst): 
    count = 0 
    for num in lst:
        if num > 0: 
            count += 1 
    lst[-1] = count 
    return lst 
print(count_positives([-1, 4, -5, 6, 7,-4])) 

#3
# total sum: a function that takes a list and returns the sum of all the values in the list. 
#input = a list of number \ output = the sum of all numbers in the list 

def sum_total(lst): 
    total = 0 
    for num in lst: 
        total += num 
    return total 
print(sum_total([1, 2, 3, 4])) 

# 4 
# a function that takes a list and returns the average of all the values
# input=a list of numbers / output: the average of the numbers in the list   
def average(lst):
    total = 0 
    for num in lst: 
        total += num 
    return total / len(lst) 
print(average([3,4,5]))

# 5
#  a function that takes a list and returns the length of the list
#input = a list of numbers / output = the length of the list 
#using the len (length) property 
def length(lst):
    return len(lst) 
print(length([1,2,3,4,5,6,7,8,9]))

# 6
# a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False. 
#input = a list of numbers / output = the minimum value in the list 
# first check if the list is empty using an if statement, if it is empty it will return false 
#then use a for loop to go through every element in the list and an if statement to check if it is ideed the lower value in the list 

def minimum(lst): 
    if len(lst) == 0: 
        return False
    min_value = lst[0] #this will start the comparison with the first element 
    for num in lst: 
        if num < min_value: 
            min_value = num 
    return min_value 
print(minimum([1,2,3,4,5]))

# 7
# a function that takes a list and returns the maximum value in the list. If the list is. empty, have the function return False
# #input = a list of numbers / output = the maximum value in the list 
# first check if the list is empty using an if statement, if it is empty it will return false  
#then use a for loop to go through every element in the list and an if statement to check if it is ideed the maximum value in the list 

def maximum(lst): 
    if len(lst) == 0: 
        return False 
    max_value = lst[0] #this will start the comparison with the first element 
    for num in lst: 
        if num > max_value: 
            max_value = num 
    return max_value 
print(maximum([1,2,3,4,5]))


# 8
# a function that takes a list and returns a dictionary that has the sum Total, average, minimum, maximum and length of the list.  
#input = a list of numbers \ output = the sum, average, minimum, maximum, and length 
#using a for loop through every number the function will add it to the total, copare it with the current minimum and the current maximum 

def ultimate_analysis(lst): 
    total = 0 
    min_value = lst[0] #this will start the comparison with the first element 
    max_value = lst[0] #this will start the comparison with the first element 
    for num in lst: 
        total += num
        if num < min_value: 
            min_value = num 
        if num > max_value: 
            max_value = num 
    return { "sumTotal": total, 
    "average": total / len(lst),
    "minimum": min_value,
    "maximum": max_value, 
    "length": len(lst) }

print(ultimate_analysis([1,2,3,4,5,6,7,8,9]))

# 9
# a function that takes a list and return that list with values reversed without creating a second list. 
# input = a list of numbers \ output = the list in reverse 

def reverse_list(lst): 
    left = 0 
    right = len(lst) - 1 
    while left < right: 
        lst[left], lst[right] = lst[right], lst[left]
        left += 1 
        right -= 1 
    return lst  
print(reverse_list([1,2,3,4,5])) 

#using the built-in function 
def reverse_list(lst): 
    lst.reverse()
    return lst
print(reverse_list([1,2,3,4,5])) 
