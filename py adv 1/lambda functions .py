'''lambda functions in Python are small anonymous functions
 that are defined using the lambda keyword. They can take any number of arguments
  but can only have one expression. The expression is evaluated and returned    
  when the function is called. Lambda functions are often used for short, throwaway functions
  or as arguments to higher-order functions like map(), filter(), and sorted().
  Syntax:
  lambda arguments: expression
  Example:
  add = lambda x, y: x + y'''
# we use this function to define small functions of one line or formulas 
#for example
m = int(input("enter 1st num:- "))
n = int(input("enter 2nd num:- "))
c = lambda m,n : m*n

print(c(n,m))


