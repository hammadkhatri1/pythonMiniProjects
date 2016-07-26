def add():
    try:
        id=int(input("Enter id: "))
        name=input("Enter name: ")
        with open("filing.txt","a") as file_2:
            file_2.write(str(id)+"     "+name+"\n")
    except Exception as eli:
        print ("Error writing to file",eli)
    else:
        print ("\nwritten succesfully\n")

def read():
    with open("filing.txt","r") as file_2:
        print("-----------------------")
        print ("ID     Names")
        print(file_2.read())
        print("-----------------------")

def menu():
    print ("  SYSTEM")
    print ("1: ADD")
    print ("2: READ")
    print ("    0: EXIT")

try:
    while(True):
        menu()
        dec=int(input("Your Decision:  "))
        if(dec==1):
            add()
        elif(dec==2):
            read()
        elif(dec==0):
            exit()
except Exception:
    print("error in main\n")