import socket
import time




#function to wait for acknowlegment
def waitingforAcknowlegment(i):
    c.settimeout(30)
    ACK_Request="Request"
    print("Waiting for Acknowlegement For Frame Number #",i)
    print("\n\n")
    c.send(ACK_Request.encode())
    try:
        ack=c.recv(1024)
        if ack.decode()=='1':
            return (1,k+1)
        else:
            return (0,k)
    except socket.timeout:
        print("\n\nOops TimeOut!!!!\n\n")
        return (0,k)
        
        
        
#sending frames to receiver    
def Sending_Frames_with_window_Size(k,n):
    for i in range(int(k),int(n)):
        if i<int(N):
            print("Sending Frame Number #",i)
            print()
            c.send(str(i).encode())
            time.sleep(2)
        
        
#sending frame when positive acknowlege receive        
def Send_frame_Ahead(k):
    print("Sending Frame Number #",k)
    print()
    c.send(str(k).encode())


#Print Discarded Frames.
def Discarded_Frames(k,n):
    for i in range(int(k),int(n)):
        if i<int(N):
            print("Discarded Frame Number #",i)
            print()


# take the server name and port name
host = 'local host'
port = 5000


#Message of Success
Success="Success"


# create a socket at sender side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   
# bind the socket with sender
# and port number
s.bind(('', port))
   
# allow maximum 1 connection to the socket
s.listen(1)
   
# wait till a client accept
# connection
c, addr = s.accept()
   
# display client address
print("CONNECTION Establishied:", str(addr))


k=0

#N indicated No of Frames tobe Transmitted
N=input("Enter the no of frames:")

#Window Size of The frames!
window_size=input("Enter the Window_size:")
#Sending Window Size to Receiver
c.send(str(window_size).encode())

#Sending  No of Frames to The Receiver
c.send(str(N).encode())


Sending_Frames_with_window_Size(k,window_size)
#loop Continue till All frames transmitted
while True:
    #waiting for Acknowledgement from the Receiver
    (ack,k)=waitingforAcknowlegment(k)
    
    
    #if Negative Acknowledgement or timeout occurs
    if ack==0:
        print("--------Discarded Frames-------\n\n")
        Discarded_Frames(k,k+int(window_size))
        print("-------Re-Sending Frames------\n\n")
        Sending_Frames_with_window_Size(k,k+int(window_size))
    #if positive Acknowledge received.
    else:

        if (k+int(window_size)-1) < int(N):
            Send_frame_Ahead(k+int(window_size)-1)
        

    #when all the Frames are Transmitted then it Ends
    if k==int(N):
        c.send(str(Success).encode())
        print("\n\n------------All Frames are Transmitted Successfully!!!!-------------------------")
        break
        

