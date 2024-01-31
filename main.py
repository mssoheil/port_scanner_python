import socket
import datetime
from colorama import Fore

def scanPort(target: str):
    try:
        ip = socket.gethostbyname(target)
        print(f"scanning target {ip}")
        print("Time start: ", datetime.datetime.now())

        for port in range(20,90):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(Fore.GREEN + "Port {}: Open".format(port))
            sock.close()

    except socket.gaierror:
        print("Host could not resolved")
    except socket.error:
        print("could not connect to server")

def main():
    target = input("enter the ip to scan: ")
    scanPort(target)


if __name__ == "__main__":
    main()