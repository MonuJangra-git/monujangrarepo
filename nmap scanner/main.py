import nmap
import sys

scanner = nmap.PortScanner()
print("welcome to simple nmap")
print("<-------------------------------------------------->")
# taking input from user for ip address and type of scan
ip_addrs = input("enter ip address :- ")
# choosing type of scan
resp = input('''which type of scan you want 
                1. SYN ACK scan
                2. UDP scan
                3. compressive scan ''')
# conditional statements to check which type of scan user wants
if resp == '1':
    # printing nmap version
    print(nmap.__version__)
    print("this may take some time please wait...")
    # calling scan method
    scanner.scan(ip_addrs,'1-1000','-sS -v')
    # printing scan information
    print(scanner.scaninfo())
    # printing ip status
    print("ip status is :- ", scanner[ip_addrs].state())
    # printing all protocols
    print(scanner[ip_addrs].all_protocols())
    # printing open ports
    if 'tcp' in scanner[ip_addrs]:
        print(scanner[ip_addrs]['tcp'].keys())

elif resp == '2':
    print(nmap.__version__)
    print("this may take some time please wait...")
    (scanner.scan(ip_addrs,'1-1000','-sU -v'))
    print(scanner.scaninfo())
    print("ip status is :- ", scanner[ip_addrs].state())
    print(scanner[ip_addrs].all_protocols())
    if 'tcp' in scanner[ip_addrs]:
        print(scanner[ip_addrs]['udp'].keys()) 
elif resp == '3':
    print(nmap.__version__)
    print("this may take some time please wait...")

    (scanner.scan(ip_addrs,'1-1000','-sS -v -A -O '))
    print(scanner.scaninfo())
    print("ip status is :- ", scanner[ip_addrs].state())
    print(scanner[ip_addrs].all_protocols())
    if 'tcp' in scanner[ip_addrs]:
        print(scanner[ip_addrs]['tcp'].keys())
else :
    print("please enter correct option")
    sys.exit()
    # to exit from the program if wrong option is selected
    # saving scan results to a file
if resp in ['1', '2', '3']:    
    with open("scan_results.txt", "a") as f:
        f.write(f"Scan results for {ip_addrs}:\n")
        f.write(str(scanner[ip_addrs]))
        f.write("\n\n")
        
        print("scan results saved in scan_results.txt")







