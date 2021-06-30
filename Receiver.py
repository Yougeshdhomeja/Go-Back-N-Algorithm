
import socket
import time  

#Sending Acknowlegment
def Sending_Acknowledgement(k):
    print("\n\nSending Acknowledgment for ",k)
    ack=input("1-Yes\n2-N0\n\nEnter Choice:")
    s.send(ack.encode())
    if ack=='2':
        print("Discarded Remaining Frames!\n\n")
        return k
    elif ack=='1':
        k=k+1
        return k
    else:
        return k
    

# take the server name and port name
   
host = 'local host'
port = 5000
  
# create a socket at client side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   
# connect it to server and port 
# number on local computer.
s.connect(('127.0.0.1', port))

#Receiving Window Size
window_size=s.recv(1024)
#Receiving number of frames
N=s.recv(1024)

k=0
#loop conitnue till all Success Message is not sent by Sender
while True:
    #frame received
    frame= s.recv(1024)
    if frame.decode()=="Request":
        k=Sending_Acknowledgement(k)
        continue
    if frame.decode()=="Success":
        s.close()
        break
    if frame.decode().find("Request")==-1:
        print("Receiving Frame Number #",frame.decode())
        print("\n\n")
    
        

