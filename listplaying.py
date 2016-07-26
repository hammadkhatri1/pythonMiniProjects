imei_list={}

def view():
    for item in imei_list:
        #print (item," | " ,imei_list[item] )
        nam=item
        im=imei_list[item]
        print("-------------------------------------")
        print ("imei:  ",im)
        print ("name:  ",nam)
    print("-------------------------------------")

def addition():
    imei=input("What is the imei: ")
    name=input("What is the name: ")
    imei_list[name]=imei


def delete():
    val=input("Enter name:  ")
    yes_or_no=input("y for confirm:  ")
    if(yes_or_no=='y'):
        imei_list.pop(val,None)
        print("DELETED")
    else:
        print ("Not delete")
while(True):
    print()
    print ("    ####   IMEI MANAGEMENT SYSTEM    ####  ") 
    decision=int(input(" 1: TO ADD\n 2: TO VIEW\n 3: TO DELETE\n 4: UPDATE \n  0: EXIT\n your decision:   "))
    
    if(decision==1):
        addition()
    elif(decision==2):
        view()
    elif(decision==3):
        delete()
    elif(decision==0):
        exit()
