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
    print(scanner[ip_addrs]['tcp'].keys())

elif resp == '2':
    print(nmap.__version__)
    (scanner.scan(ip_addrs,'1-2000','-sU -v'))
    print(scanner.scaninfo())
    print("ip status is :- ", scanner[ip_addrs].state())
    print(scanner[ip_addrs].all_protocols())
    print(scanner[ip_addrs]['udp'].keys()) 
elif resp == '3':
    print(nmap.__version__)
    (scanner.scan(ip_addrs,'1-2000','-sU -v -A -O '))
    print(scanner.scaninfo())
    print("ip status is :- ", scanner[ip_addrs].state())
    print(scanner[ip_addrs].all_protocols())
    print(scanner[ip_addrs]['tcp'].keys())
else :
    print("please enter correct option")









