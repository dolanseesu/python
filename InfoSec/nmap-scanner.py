#! /usr/bin/python3

'''
A small script that executes different nmap scans

Part of this is still broken and the output needs to be formated properly
'''

import nmap
import time

scanner = nmap.PortScanner()

print('--- Small Python nmap automation script ---')

ip_addr = input('Please enter the IP to scan: ')
ports = '1-1024'    # maybe make this interactive in the future


cmd = input('''\nPlease enter the type of scan:
               1) TCP Scan
               2) UDP Scan
               3) Comprehensive Scan\n''')

if cmd == '1':
    start_time = time.time()

    print('Nmap version: ', str(scanner.nmap_version()[0]) + '.' + str(scanner.nmap_version()[1]))
    scanner.scan(ip_addr, ports, '-v -sS')
    print(scanner.scaninfo())
    print('IP Status: ', scanner[ip_addr].state())

    print('Open Ports: ', end='') 
    for i in scanner[ip_addr]['tcp'].keys():
        print(i, '', end='')

    print(f'\nFinished in {round(time.time() - start_time, 2)} seconds')
    print(scanner[ip_addr])

elif cmd == '2':
    start_time = time.time()

    print('Nmap version: ', str(scanner.nmap_version()[0]) + '.' + str(scanner.nmap_version()[1]))
    scanner.scan(ip_addr, ports, '-v -sU')
    print(scanner.scaninfo())
    print('IP Status: ', scanner[ip_addr].state())
    print('Open Ports: ', scanner[ip_addr]['udp'].keys())
    
    print(f'\nFinished in {round(time.time() - start_time, 2)} seconds')

elif cmd == '3':
    start_time = time.time()

    print('Nmap version: ', str(scanner.nmap_version()[0]) + '.' + str(scanner.nmap_version()[1]))
    scanner.scan(ip_addr, ports, '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print('IP Status: ', scanner[ip_addr].state())
    print('Open Ports: ', scanner[ip_addr]['tcp'].keys())

    print(f'Finished in {round(time.time() - start_time, 2)} seconds')

else:
    print('Please enter a number between 1 and 3.')