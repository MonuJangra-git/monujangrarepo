from datetime import datetime
print("welcome to your diary \nyou can write as much you want\n save your informatiom in diary ")
print("press s for search and t for text")

for i in range(1,100):
    ipt = input("you want to :-").strip().lower()
    if(ipt == 's'):
        with open("diary.txt","r") as f:

            l1 = f.readline()
            line = 1
            search = input("search :- ").strip()
            while l1 != "" :
                if search in l1 : 
                    print(f"{search} present is in line no. {line} ")
                    print(l1)
        
                l1 = f.readline()
                line +=1
    
    
   
    


    if(ipt == 't'):
        with open("diary.txt","a") as f:

            print("press n for next line any key for exit")
            print("enter which you want to write in your diary\n")
            for i in range(1,100000):
                    inp = input(f" {i} ")
                    f.write(f" {inp} \n")
                    cmd = input("")
                    if( cmd != "n" ):
                        print("thanks for writting")
                        break   

 
      
    
      

    if ipt not in ['s','t']: 
           print("you put wrong info") 
    print("if want to continue operations on diary then\n press yes for yes \n no for not ")    
    conf = input("enter :- ")
    if conf == "yes":
        print("ok you can continue")
    else :
        print("have a good day")
        break    
# for adding timestamp to diary entries
with open("diary.txt","a") as f:
    ipt = s = "search"
    ipt = t = "text"
    f.write(f"[{datetime.now()}] {ipt}\n")






