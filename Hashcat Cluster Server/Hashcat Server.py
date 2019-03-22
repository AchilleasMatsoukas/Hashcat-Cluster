import socket
import sys
import traceback
import threading
import time
from array import *

# Evilnight Programming
# Achilleas Matsoukas
# Version 1.0

# Global Variables
Start = [0, 0, 0, 0, 0, 0, 0, 0, -1, 100, 100, 100, 100, 100, 100, 100]
lock = threading.Lock()
# 16 chars

# Functions
def main():
    start_server()


def start_server():
    print(r"""
    
    ########### Hashcat Cluster Server ############   
            
        Art by Morfina

         _                  _   
        | '-.            .-' |
        | -. '..\\,.//,.' .- |
        |   \  \\\||///  /   |
       /|    )M\/%%%%/\/(  . |\
      (/\  MM\/%/\||/%\\/MM  /\)
      (//M   \%\\\%%//%//   M\\)
    (// M________ /\ ________M \\)
     (// M\ \(',)|  |(',)/ /M \\) \\\\  
      (\\ M\.  /,\\//,\  ./M //)
        / MMmm( \\||// )mmMM \  \\
         // MMM\\\||///MMM \\ \\
          \//''\)/||\(/''\\/ \\
          mrf\\( \oo/ )\\\/\
              \'-..-'\/\\
                  \\/ \\


                        Made by: Evilnight Porgramming
                        Ver: 1.0
                        
                    """)
    print("\n\nServer is Initializing...")
    print("## If you want to run this script local use LOCAL_IP and a PORT of your choice. For internet use, use your PUBLIC_IP and you forwarded PORT ##")
    print("## Use ifconfig (Linux) or ipconfig (Windows) to determinate your LOCAL_IP ##")
    print("## Press CTRL+C or CTRL+Z if you want to exit ##")

    IP_Address = input("\n\nIP = ")
    Port = input("Port = ")
    Port = int(Port)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    while(1):
        try:
            server.bind((IP_Address, Port))
            break
        except:
            print("## Bind Failed. Error : IP Address or port can't connect ##")
            IP_Address = input("\nIP = ")
            Port = input("Port = ")
            Port = int(Port)

    server.listen(10)
    print("Socket is now listening...")

    while True:
        conn, address = server.accept()
        client_ip, client_port = str(address[0]), str(address[1])
        print("\n[+] New connection from ip: " + client_ip + ":" + client_port)

        try:
            threading.Thread(target=ClientThread, args=(conn, client_ip, client_port)).start()
        except:
            print("Client Thread Failed to Start.")
            traceback.print_exc()


    server.close()


def ClientThread(conn, ip, port, buffer = 1024):
    print("[+] Client thread for " + ip + ":" + port + " just started")
    is_active = True
    global Start

    while is_active:
        client_input = receive_input(conn, buffer)

        if "--quit--" in client_input:
            print("Client with " + ip + ":" + port + " is requesting to quit")
            conn.close()
            print("Connection successfully closed")
            is_active = False
        elif "hccapx" in client_input:
            Send_HCCAPX(conn, ip, port)
            client_input = receive_input(conn, buffer)
        elif "start" in client_input:
            lock.acquire()
            Send_Start(conn, ip, port, Start)
            Count_next()
            #print(Start)
            lock.release()
            client_input = receive_input(conn, buffer)
        elif "wordlist" in client_input:
            Wordlist(conn, ip, port)
            client_input = receive_input(conn, buffer)
        elif "crack" in client_input:
            Hashcat(conn, ip, port)
        elif "POSITIVE" in client_input:
            print("\n\n---- PASSWORD FOUND TERMINATING AND PRINTING IT---\n\n")
            print("password ==> " + client_input[2:-12])
            is_active = False
        elif "NEGATIVE" in client_input:
            print("[" + ip + ":" + port + "] Client exhausted the wordlist... and will restart")
        else:
            pass
            #client_input = client_input[2:-1]
            #print("Processed Result: {}".format(client_input))
            #conn.send("Hello".encode("utf8"))


def receive_input(conn, buffer):
    client_input = conn.recv(buffer)
    client_input_size = sys.getsizeof(client_input)

    if client_input_size > buffer:
        print("The input size is greater than expected {}".format(client_input_size))

    decoded_input = client_input.decode("utf8").rstrip()
    result = str(client_input)
    return result


def Send_HCCAPX(server, ip, port):
    #hccapx = open('hashcat.hccapx', 'rb')
    print("[" + ip + ":" + port + "] ""Preparing HCCAPX file...")
    file = open('hashcat.hccapx', "rb")
    print("[" + ip + ":" + port + "] " + "[+] Sending HCCAPX...")
    data = file.read(1024)
    #print(data)
    server.sendall(data)
    file.close()
    print("[" + ip + ":" + port + "] " + "Done Sending!")
    time.sleep(1)


def Send_Start(conn, ip, port, startp):
    print("[" + ip + ":" + port + "] ""Sending Starting point to Client...")
    str1 = ','.join(str(e) for e in startp)
    bytesl = bytes(str1, 'utf-8')
    conn.send(bytesl)
    print("[" + ip + ":" + port + "] " + "Done Sending!")


def Count_next():
    global Start
    print("[Current Progress] " + str(Start))
    i = 1
    while 1:
        if Start[len(Start) - i] == 100:
            i = i + 1
        else:
            break
    end_of_pass = len(Start) - i
    # print(end_of_pass)
    f = False
    for i in range(100000000):
        Start[end_of_pass] = Start[end_of_pass] + 1
        for o in range(end_of_pass, 0, -1):
            if Start[o] == 84:
                Start[o] = 0
                Start[o - 1] = Start[o - 1] + 1
                if Start[o - 1] > 84:
                    Start[o - 1] = 83
            else:
                break
        if Start[0] == 84:
            for k in range(1, end_of_pass + 1):
                if Start[k] == 83:
                    f = True
                else:
                    f = False
                    break
            if f == True:
                end_of_pass = end_of_pass + 1
                for k in range(0, end_of_pass):
                    Start[k] = 0
                Start[end_of_pass] = 0



def Wordlist(conn, ip, port):
    print("[" + ip + ":" + port + "] " + "Client has created his Wordlist...")


def Hashcat(conn, ip, port):
    print("[" + ip + ":" + port + "] " + "Hashcat Subprogram started...")
# End of Functions

# Core Program
if __name__ == "__main__":
    main()