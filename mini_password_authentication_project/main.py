from file import dic
# Function to authenticate user
#you can modify the function as per your requirement
#you can add more dictionary or database calls here

def authent(username,passwd):
    if username in dic and dic[username]==passwd:
        print(f"authentication successfull \n your username :-{username} \n password :- {passwd}")

        return True 
    print("enter correct useranme ")
    
    return False


usernm = input("enter username")
passt = input("enter password :- ")
authent(usernm,passt)
if authent(usernm,passt) == True:
    # do something
    #your code here
    #you can make function calls or any other operations
    print("Access Granted")
    pass 
