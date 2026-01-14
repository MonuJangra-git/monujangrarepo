lis = []
i = 1
typ = int(input("you want to find highest number press 1 or lowest number press 2:- "))
if typ != 1 and typ != 2 :
    print("invalid input")
while True:

    inp = (input("enter number"))
    if inp == "stop":
        break 
    try :
        num = int(inp)     
        lis.append(num)
    
    except Exception as error :
        print("error")    
    

if typ == 1 :
    print(max(lis))
if typ == 2 :
    print(min(lis))  
    




# this is for extra knowledge based on concept

# while c < d :
#     print(lis[c])
#     c+=1
# hig = lis[0]
# k=0
# while k<d:
#     if lis[k]>hig:
#         hig = lis[k]

#     k+=1    

# print(hig)
# print(max(lis))
# print(min(lis))
'''if we want to find lowest number
    then we can use below code'''
# k=0
# low = lis[0]
# while k<d:
#     if lis[k]<low:
#         low = lis[k]
#     k+=1  
# print(low)  
# print(min(lis))
#by using this we can find highest and lowest number