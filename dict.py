imei_list={}

while(True):
    print ("\n  ***IMEI MANAGEMENT SYSTEM***")
    dec=int(input(" 1: ADD \n 2: VIEW \n 3: DELETE \n  0: TO EXIT\nYour decision:  "))
    
    if(dec==1):
        imei=input("Enter Imei: ")
        name=input("Enter name: ")
        imei_list[imei]=name
    elif(dec==2):
        print (imei_list)
    elif(dec==0):
        exit()