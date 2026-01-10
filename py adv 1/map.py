'''map() function in Python applies a given function 
to all items in an input 
list (or any iterable) and
 returns an iterator (map object) with the results. 
It is commonly used for transforming data 
in a concise and efficient manner.
Syntax: name = map(function, iterable)
Example:
def square(x):
    return x * x
    numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]'''
# we can also use lambda functions with map function to make it more concise
numbers = [1,2,3,4,5,6,7,8,9,10]
squared_numbers = map(lambda x: x*x , numbers)
print(list(squared_numbers))
# we can also use map function with multiple iterables  
numbers1 = [1,2,3]
numbers2 = [4,5,6]  
summed_numbers = map(lambda x,y: x+y , numbers1 , numbers2)
print(list(summed_numbers))
# we can also use built in functions with map function
string_numbers = ['1','2','3','4','5']
int_numbers = map(int , string_numbers)
print(list(int_numbers))

# we can also use custom functions with map function
def cube(x):
    return x**3
cubed_numbers = map(cube , numbers)
print(list(cubed_numbers))      
# map function is very useful when we have to apply same operation on multiple items
# it is more efficient then using for loop to iterate through each item and apply operation
# also map function returns an iterator which is more memory efficient then list    
# overall map function is a powerful tool in python for data transformation and manipulation
# it is widely used in data science and machine learning for preprocessing data
# thus always consider using map function when you have to apply same operation on multiple items
# it will make your code more concise , efficient and readable
# thank you
# we can also convert map object to other data types like list , tuple , set etc
map_obj = map(lambda x: x+1 , numbers)
print(tuple(map_obj))  # converting to tuple
map_obj = map(lambda x: x*2 , numbers)
print(set(map_obj))    # converting to set
map_obj = map(lambda x: x-1 , numbers)
print(list(map_obj))   # converting to list
# once map object is converted to other data type it can not be used again
# we have to create new map object to use it again      
# also we can chain multiple map functions together
map_obj = map(lambda x: x+1 , numbers)
map_obj = map(lambda x: x*2 , map_obj)  
print(list(map_obj))
# in above example first map function adds 1 to each item and second map function multiplies
# the result by 2
# thus chaining multiple map functions can be useful in some cases
# but it may also make code less readable
# so use it judiciously
# finally we can also use map function with filter function to filter and transform data
filtered_numbers = filter(lambda x: x%2==0 , numbers)  # filtering even
mapped_numbers = map(lambda x: x*x , filtered_numbers) # squaring
print(list(mapped_numbers))
# in above example first filter function filters even numbers and then map function squares them
# thus combining map and filter functions can be powerful tool for data processing
# thank you
# this is how map function works in python
# hope you understood it well
# if you have any doubts feel free to ask
# happy coding
# by monu jangra
