import sys
import ipaddress
import fromIP
import fromFN
import fromU
import asyncio

def ip_validator(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

args = sys.argv
if args.__len__() > 1:
    match args[1]:
        case "--help" | "-h" :
            print("Welcome to passive v1.0.0\n\nOPTIONS:\n    -fn         Search with full-name\n    -ip         Search with ip address\n    -u          Search with username\n")
        case "-fn":
            if args.__len__() != 3:
                print("Error Option")
            fn = args[2]
            fromFN.search_pages_blanches(fn)
        case "-ip":
            if args.__len__() != 3:
                print("Error Option")
            ip = args[2]
            if ip_validator(ip) == True :
                # recuperer les informations   
                fromIP.Ip(ip)
            else :
                print("Error ip address")
        case "-u":
            if args.__len__() != 3:
                print("Error Option")
            login = args[2]
            if login.startswith("@"):
                # Lancer l'async main
                fromU.search_profile(login)
            else:
                print("Error of login")