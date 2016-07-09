#!/usr/bin/env python

"""
This program parse the given hosts file and return the IP address of a given computers list

"""
__author__ = 'Eabel'

import sys
import os
import argparse
import socket
from collections import defaultdict




def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True

def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True

def is_valid_ip(address):
    return is_valid_ipv4_address or is_valid_ipv6_address(address)

def is_valid_file_path(file_path):
    if os.path.isfile(file_path):
        return True
    else :      
        print "Error - invalid file path",file_path
        return False




def read_hosts_file(file_path):
    if not is_valid_file_path(file_path):
        sys.exit()
    f = open(file_path)
    host_dict = defaultdict(str)
    for line in f:
        items = line.split('=')
        if len(items) != 2:
            return False;
        if not is_valid_ip(items[1]):
            return False;
        host_dict[items[0]] = items[1].rstrip('\r\n')
    return host_dict

def get_ip(machine,host_dict):
    ip = host_dict[machine];
    if not ip:
        print 'Error -',machine,'is missing from hosts file'
        sys.exit()
    return ip


########################################################################################################################
#
#
def main():
    parser = argparse.ArgumentParser(description='This program parse the given hosts file and return the IP address of a given computers list')
    
    parser.add_argument("hosts_path", help="path to the host file")
    args = parser.parse_args()   

    host_dict = read_hosts_file(args.hosts_path)

    machines = raw_input("Please enter list of machines names (i.e name1 name2 ...):\n").split()

    ip_list = [get_ip(machine,host_dict) for machine in machines] 
    print ip_list;
        
if __name__ == '__main__':
    main()
