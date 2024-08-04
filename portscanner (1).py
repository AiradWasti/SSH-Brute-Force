#!/usr/bin/python
from socket import *
import argparse
from threading import Thread, Lock
from termcolor import colored

print_lock = Lock()

def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((tgtHost, tgtPort))
        with print_lock:
            print(colored('%d/tcp Open' % tgtPort, 'magenta'))
    except (OSError, ConnectionRefusedError):
        with print_lock:
            print(colored("%d/tcp Closed" % tgtPort, 'red'))
    finally:
        sock.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except gaierror:
        print(colored("Unknown Host %s" % tgtHost, 'red'))
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print(colored("Scan Results for: " + tgtName[0], 'cyan'))
    except herror:
        print(colored("Scan results for: " + tgtIP, 'cyan'))
    
    setdefaulttimeout(1)
    
    threads = []
    
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

def main():
    parser = argparse.ArgumentParser(description='Usage of program: -H <target host> -P <target ports separated by comma>')
    parser.add_argument('-H', dest='tgtHost', type=str, required=True, help='specify target host')
    parser.add_argument('-P', dest='tgtPort', type=str, required=True, help='specify target ports separated by comma')
    args = parser.parse_args()

    tgtHost = args.tgtHost
    tgtPorts = str(args.tgtPort).split(',')
    
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()
