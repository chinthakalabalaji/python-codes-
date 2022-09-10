import socket
#import multiprocessing as mp
import time
import cv2
import os
ser=socket.socket()
ser.bind((socket.gethostname(),1233))
print(ser.getsockname())
ser.listen(5)
def view():
    """try:"""
    with open("./pro/names.txt","r") as f1:
        l=f1.read()
    f1.close()
    l=l[:len(l)-1]
    #print(l)
    li=l.split(",")
    #li.reverse()
    #print(li)
    for i in li:
        if i != "":
            l=cv2.imread("./pro/"+i,-1)
            cv2.imshow("image",l)
            cv2.waitKey(6000)
            cv2.destroyAllWindows()
    """except:
        with open("./pro/names.txt","w") as f1:
            f.write("")
        f1.close()"""
while True:
    try:
        view()
        print("Waiting for connection")
        c,add=ser.accept()
        print("Connected",add)
        #p2.acquire()
        f_name=c.recv(1024).decode("utf-8")
        if f_name:
            with open("./pro/names.txt","a") as f1:
                f1.write(f_name+",")
            f1.close()
            print(f_name)
            with open("./pro/"+f_name,"ab") as f:
                while 1:
                    l=c.recv(130990)
                    #l=c.recv(130990)
                    if len(l)<=0:
                        break
                    f.write(l)
            view()
            f.close()
            c.close()
        else:
            print("picture is not received")
            with open("./pro/names.txt","r") as f1:
                l=f1.read()
            f1.close()
            with open("./pro/names.txt","w") as f2:
                f2.write("")
            f2.close()
            l=l[:len(l)-1]
            li=l.split(",")
            for i in set(li):
                if i != "":
                    os.remove("./pro/"+i)
    except Exception as e:
        print("Error occored",e)
        c.close()

