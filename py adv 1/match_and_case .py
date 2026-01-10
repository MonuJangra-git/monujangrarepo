def status(stat) :
    match (stat):
        case stat if 0 < stat <= 90 :
            print(f"status found {stat} and you can play bgmi smoothly")
            return type("13333")
        case stat if 90 < stat <= 667 :
            print(f"status found {stat} and you can play bgmi with many lags")
        case stat if 667 < stat <= 999 :
            print(f"status found {stat} and you can't play bgmi not even hardly")
        case _:
            print("enter correct value")

ping = int(input("enter you game ping you can check your performance by\n just putting your game ping :- "))

print(status(ping))
#we use match and case to just for clean bugfree and staright froward easy to use
#so it is important 
#that's why we use it instead of many if else conditions
# it is similar like switch in C language