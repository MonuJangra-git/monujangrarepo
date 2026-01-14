#we have to find the greatest number between 4 numbers input by user
import sys

try :
    num1 = int(input("enter number1 :- "))
    num2 = int(input("enter number2 :- "))
    num3 = int(input("enter number3 :- "))
    num4 = int(input("enter number4 :- "))
except Exception as wrong :
    print("wrong input try again")
    sys.exit()
if(num1 > num2 and num1 > num3 and num1 > num4):
    print("greatest number is :-", num1)
elif(num2 > num1 and num2 > num3 and num2 > num4):
    print("greatest number is :-", num2)
elif(num3 > num1 and num3 > num2 and num3 > num4):
    print("greatest number is :-", num3)
else :
    print("the greatest number is ", num4)   


