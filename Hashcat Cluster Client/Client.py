import socket
import sys
import numpy as np
import time
import subprocess
import platform

# Evilnight Programming
# Achilleas Matsoukas
# Version 1.0

global_array = []
print_list = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

# Functions
def main():
    print(r"""

        ########### Hashcat Cluster Client ############   

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
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("## Fill the IP and PORT of the Server ##")
    host = input("\n\nIP = ")
    port = input("Port = ")
    port = int(port)

    try:
        server.connect((host, port))
    except:
        print("Connection error")
        sys.exit()
    is_active = True

    print("## Choose how many cycles you want ##")
    print("## A cycle is how many wordlists will the script get ( default wordlist is 10^8 ) ##")
    print("## Press CTRL+C or CTRL+Z  if you want to exit ##")
    cycles = input("[+] Choose how many cycles you want to do : ")
    i = 0

    message = 'hccapx'
    Receive_HCCAPX(server)

    while is_active:
        time.sleep(2)
        message = 'start'
        server.send(b'start')
        data = Receive_Start(server)
        message = 'wordlist'
        Create_list(server, data)
        message = 'crack'
        Hashcat(server)

        time.sleep(2)

        i = i + 1
        if i == int(cycles):
            print("[+] Done with all the cycles quiting... Bye")
            server.send(b'--quit--')
            terminate = input("[+] Press any button to exit...")
            exit(1)


def Receive_HCCAPX(server):
    print("[+] Requesting HCCAPX file from server...")
    file = open('hashcat.hccapx', "wb")
    server.send(b"hccapx")
    print("[+] Receiving...")
    data = server.recv(1024)
    file.write(data)
    file.close()
    print("[+] File Received!\n")


def Receive_Start(server):
    print("[+] Requesting Starting point from server...")
    server.send(b"start")
    data = server.recv(1024)
    #print(data)
    data1 = str(data, 'utf-8')
    data2 = data1.split()
    data_array = np.array(data2)
    #print(type(data_array))
    global_array.append(data_array)
    print("[+] Starting point Received...")
    return data_array


def Create_list(server, data1):
    print("[+] Generating the list...")
    data = str(data1)
    data = data[2:-2]
    list = data.split(',')
    for i in range(0, len(list)):
        list[i] = int(list[i])
    #print(list)
    file = open('wordlist.dict', "w")
    i = 1
    while 1:
        if list[len(list) - i] == 100:
            i = i + 1
        else:
            break
    end_of_pass = len(list) - i
    #print(end_of_pass)
    f = False
    for i in range(100000000):
        list[end_of_pass] = list[end_of_pass] + 1
        for o in range(end_of_pass, 0, -1):
            if list[o] == 84:
                list[o] = 0
                list[o-1] = list[o-1] + 1
                if list[o-1] > 84:
                    list[o-1] = 83
            else:
                break
        if list[0] == 84:
            for k in range(1, end_of_pass + 1):
                if list[k] == 83:
                    f = True
                else:
                    f = False
                    break
            if f == True:
                end_of_pass = end_of_pass + 1
                for k in range(0, end_of_pass):
                    list[k] = 0
                list[end_of_pass] = 0
        #print(list)
        for n in range(16):
            if(list[n] == 100):
                print_list[n] = ''
            if (list[n] == 0):
                print_list[n]= '0'
            elif (list[n] == 1):
                print_list[n] = '1'
            elif (list[n] == 2):
                print_list[n] = '2'
            elif (list[n] == 3):
                print_list[n] = '3'
            elif (list[n] == 4):
                print_list[n] = '4'
            elif (list[n] == 5):
                print_list[n] = '5'
            elif (list[n] == 6):
                print_list[n] = '6'
            elif (list[n] == 7):
                print_list[n] = '7'
            elif (list[n] == 8):
                print_list[n] = '8'
            elif (list[n] == 9):
                print_list[n] = '9'
            elif (list[n] == 10):
                print_list[n] = 'a'
            elif (list[n] == 11):
                print_list[n] = 'b'
            elif (list[n] == 12):
                print_list[n] = 'c'
            elif (list[n] == 13):
                print_list[n] = 'd'
            elif (list[n] == 14):
                print_list[n] = 'e'
            elif (list[n] == 15):
                print_list[n] = 'f'
            elif (list[n] == 16):
                print_list[n] = 'g'
            elif (list[n] == 17):
                print_list[n] = 'h'
            elif (list[n] == 18):
                print_list[n] = 'i'
            elif (list[n] == 19):
                print_list[n] = 'j'
            elif (list[n] == 20):
                print_list[n] = 'k'
            elif (list[n] == 21):
                print_list[n] = 'l'
            elif (list[n] == 22):
                print_list[n] = 'm'
            elif (list[n] == 23):
                print_list[n] = 'n'
            elif (list[n] == 24):
                print_list[n] = 'o'
            elif (list[n] == 25):
                print_list[n] = 'p'
            elif (list[n] == 26):
                print_list[n] = 'q'
            elif (list[n] == 27):
                print_list[n] = 'r'
            elif (list[n] == 28):
                print_list[n] = 's'
            elif (list[n] == 29):
                print_list[n] = 't'
            elif (list[n] == 30):
                print_list[n] = 'u'
            elif (list[n] == 31):
                print_list[n] = 'v'
            elif (list[n] == 32):
                print_list[n] = 'w'
            elif (list[n] == 33):
                print_list[n] = 'z'
            elif (list[n] == 34):
                print_list[n] = 'y'
            elif (list[n] == 35):
                print_list[n] = 'z'
            elif (list[n] == 36):
                print_list[n] = 'A'
            elif (list[n] == 37):
                print_list[n] = 'B'
            elif (list[n] == 38):
                print_list[n] = 'C'
            elif (list[n] == 39):
                print_list[n] = 'D'
            elif (list[n] == 40):
                print_list[n] = 'E'
            elif (list[n] == 41):
                print_list[n] = 'F'
            elif (list[n] == 42):
                print_list[n] = 'G'
            elif (list[n] == 43):
                print_list[n] = 'H'
            elif (list[n] == 44):
                print_list[n] = 'I'
            elif (list[n] == 45):
                print_list[n] = 'J'
            elif (list[n] == 46):
                print_list[n] = 'K'
            elif (list[n] == 47):
                print_list[n] = 'L'
            elif (list[n] == 48):
                print_list[n] = 'M'
            elif (list[n] == 49):
                print_list[n] = 'N'
            elif (list[n] == 50):
                print_list[n] = 'O'
            elif (list[n] == 51):
                print_list[n] = 'P'
            elif (list[n] == 52):
                print_list[n] = 'Q'
            elif (list[n] == 53):
                print_list[n] = 'R'
            elif (list[n] == 54):
                print_list[n] = 'S'
            elif (list[n] == 55):
                print_list[n] = 'T'
            elif (list[n] == 56):
                print_list[n] = 'U'
            elif (list[n] == 57):
                print_list[n] = 'V'
            elif (list[n] == 58):
                print_list[n] = 'W'
            elif (list[n] == 59):
                print_list[n] = 'X'
            elif (list[n] == 60):
                print_list[n] = 'Y'
            elif (list[n] == 61):
                print_list[n] = 'Z'
            elif (list[n] == 62):
                print_list[n] = '!'
            elif (list[n] == 63):
                print_list[n] = '@'
            elif (list[n] == 64):
                print_list[n] = '#'
            elif (list[n] == 65):
                print_list[n] = '$'
            elif (list[n] == 66):
                print_list[n] = '%'
            elif (list[n] == 67):
                print_list[n] = '^'
            elif (list[n] == 68):
                print_list[n] = '&'
            elif (list[n] == 69):
                print_list[n] = '*'
            elif (list[n] == 70):
                print_list[n] = '('
            elif (list[n] == 71):
                print_list[n] = ')'
            elif (list[n] == 72):
                print_list[n] = '_'
            elif (list[n] == 73):
                print_list[n] = '+'
            elif (list[n] == 74):
                print_list[n] = '='
            elif (list[n] == 75):
                print_list[n] = ';'
            elif (list[n] == 76):
                print_list[n] = '?'
            elif (list[n] == 77):
                print_list[n] = '>'
            elif (list[n] == 78):
                print_list[n] = '<'
            elif (list[n] == 79):
                print_list[n] = '['
            elif (list[n] == 80):
                print_list[n] = ']'
            elif (list[n] == 81):
                print_list[n] = '{'
            elif (list[n] == 82):
                print_list[n] = '}'
            elif (list[n] == 83):
                print_list[n] = '/'
            elif (list[n] == 84):
                print_list[n] = ' '

        string = ''.join(print_list)
        file.write(string + '\n')
        if (i % 1000000 == 0):
           progress = (float(i)/100000000) * 100
           print("{:.0f}".format(progress) + "%")
    file.close()
    print("[+] Generation of Wordlist Done...")


def Hashcat(server):
     #server.send(b'crack')
    OS = platform.system()
    #print(OS)
    if OS == "Windows":
        command =".\hashcat32.exe -m 2500 hashcat.hccapx wordlist.dict"
        hashcat = subprocess.call(command, shell=True)

        file = open('hashcat.potfile', "r")
        result = file.read(1024)
        if result == "":
            print("[+] Hashcat didn't crack the password...")
            time.sleep(5)
            server.send(b'NEGATIVE')
            server.send(b'NEGATIVE')
        else:
            result_list = result.split(":")
            password = result_list[len(result_list)-1]
            #print(password)
            time.sleep(5)
            passwordb = password + " POSITIVE"
            passwordb = passwordb.encode()
            server.send(passwordb)
    elif OS == "Linux":
        command ="hashcat -m 2500 hashcat.hccapx wordlist.dict"
        hashcat = subprocess.call(command, shell=True)

        file = open('/root/.hashcat/hashcat.potfile', "r")
        result = file.read(1024)
        if result == "":
            print("[+] Hashcat didn't crack the password...")
            time.sleep(5)
            server.send(b'NEGATIVE')
            server.send(b'NEGATIVE')
        else:
            result_list = result.split(":")
            password = result_list[len(result_list)-1]
            #print(password)
            time.sleep(5)
            passwordb = password + " POSITIVE"
            passwordb = passwordb.encode()
            server.send(passwordb)
# End of Functions

if __name__ == "__main__":
    main()