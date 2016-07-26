def menu():
    print ("  ---MENU---- ")
    print ("1: Add")
    print ("2: Read")
    print ("3: Search")
    print ("    0: EXIT")

def add():
    try:
        id=int(input("Enter ID:  "))
        name=input("Enter name:  ")
        clas=input("Enter class:  ")
        sec=input("Enter section:  ")
        with open("management.txt","a") as file_1:
            file_1.write(str(id)+"  | "+name+"      | "+clas+"-"+sec+"\n")
    except Exception as e:
        print (e)
    else:
        print ("Writin successfully")


def read():
    try:   
        with open("management.txt","r") as file_2:
            print("-----------------------")
            print ("ID | Names      |   Class-Section  ")
            print(file_2.read())
            print("-----------------------")
    except Exception as e:
        print (e)

def search():
    id=input("Enter id: ")
    with open("management.txt","r") as file_1:
        for line in file_1:
            if(id in line):
                print ("\nID | Names      |   Class-Section  ")
                print (line)
                print ()
                break
def main():
    while (True):
        try:
            menu()
            dec=int(input("decision:  "))
            if(dec==1):
                add()
            elif(dec==2):
                read()
            elif(dec==3):
                search()     
            elif(dec==0):
                print("     G00D BYE")
                exit()
        except Exception as e:
            print (e)

print ("\n  *****   Student Management System *****\n")
main()