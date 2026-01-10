'''
The walrus operator (:=) was introduced in Python 3.8.
It allows you to assign a value to a variable as part of an expression.
 Why it’s useful
Normally, assignment (=) and evaluation are separate. With :=, you can:
Save intermediate results without repeating code.
Make loops and conditions more concise.
Improve readability in some cases.
'''
# lenght = [1,2,3,4,5]
# leng = len(lenght)
# if leng > 5:
#     print("list has lenght greater then 5")
# elif leng < 5:
#     print("list has lenght less then 5")
# elif leng == 5:
#     print("list has lenght equal to 5")

# we can also use this using walrus operator like
if leng :=len([1,2,3,4,5,6]) > 5:
    print("list has lenght greater then 5")
    # may add more conditions 
# but some time it may make proggram complictad
# Without walrus
line = input("Enter text: ")
while line != "quit":
    print(f"You entered: {line}")
    line = input("Enter text: ")

# With walrus
while (line := input("Enter text: ")) != "quit":
    print(f"You entered: {line}")
# List comprehension
# Using walrus to filter and store values
nums = [1, 2, 3, 4, 5]
squares = [sq for n in nums if (sq := n*n) > 10]
    #  sq is both calculated and checked in the same expressif fon.