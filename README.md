# Hashcat-Cluster
  A script developed using Python and the original Hashcat to create a bruteforce WPA password cracker.
  
# Requirements
  Windows : Python 3 and higher and for the Client to run properly use pip to install Numpy
  Linux : Python 3 and higher with Numpy installer

# Installation
  Windows :
      Client: Extract the Hashcat.zip file into a folder and then run the Script using pythons console.
      Server: Just put the script into a folder and the Handshake your want to crack.
  Linux :
      Client: Run those commands 1) sudo apt-get install python3-pip 2) sudo pip3 install numpy then just put the client in a                 
              folder and give them permissions. 

# Usage
  Client: After having the IP:PORT of the server run the client using :~# python3 Client.py IP:PORT
  You will be asked for the number of Cycles once your fill your credentials.
  CYCLES : Is the number of times the client will loop. (For stable results use arounds 20-40 depending on your hardware.
   
  Server: Get the hccapx file you want to crack and put it into the same folder as the script.Find your LOCAL_IP or your forwarded 
  one with the port and run the script using :~#python3 Server.py. After that once a client connect it will automatically assign 
  some workload to crack.
