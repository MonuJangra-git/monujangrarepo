import nmap

scanner = nmap.PortScanner()
print("welcome to simple nmap")
print("<-------------------------------------------------->")
ip_addrs = input("enter ip address :- ")
resp = input('''which type of scan you want 
                1. SYN ACK scan
                2. UDP scan
                3. compressive scan ''')
if resp == '1':
    print(nmap.__version__)
    (scanner.scan(ip_addrs,'1-2000','-sS -v'))
    print(scanner.scaninfo())
    print("ip status is :- ", scanner[ip_addrs].state())
    print(scanner[ip_addrs].all_protocols())
    if 'tcp' in scanner[ip_addrs]:
        print(scanner[ip_addrs]['tcp'].keys())

elif resp == '2':
    print(nmap.__version__)
    (scanner.scan(ip_addrs,'1-2000','-sU -v'))
    print(scanner.scaninfo())
    print("ip status is :- ", scanner[ip_addrs].state())
    print(scanner[ip_addrs].all_protocols())
    if 'tcp' in scanner[ip_addrs]:
        print(scanner[ip_addrs]['udp'].keys()) 
elif resp == '3':
    print(nmap.__version__)
    (scanner.scan(ip_addrs,'1-2000','-sS -v -A -O '))
    print(scanner.scaninfo())
    print("ip status is :- ", scanner[ip_addrs].state())
    print(scanner[ip_addrs].all_protocols())
    if 'tcp' in scanner[ip_addrs]:
        print(scanner[ip_addrs]['tcp'].keys())
else :
    print("please enter correct option")
    sys.exit()

with open("scan_results.txt", "a") as f:
    f.write(str(scanner[ip_addrs]))
print("scan results saved in scan_results.txt")







