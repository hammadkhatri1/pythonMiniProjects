
def calculator(type):
    print("\n *******",type.upper(),"CALCULATOR**************")
    print ("1: addition \n2: subtraction \n3: multiplication\n 4: division")
    dec=input("Enter choice(1/2/3/4):")

    val1=int(input("Enter first number: "))
    val2=int(input("Enter second number: "))

    if(dec=='1'):
        print (val1," + ",val2 ,' = ',val1+val2)
    elif(dec=='2'):
        print (val1," - ",val2," = ",val1-val2)
    elif(dec=='3'):
        print (val1," * ",val2," = ",val1*val2)
    elif(dec=='4'):
        print (val1," / ",val2," = ",val1/val2)
    else :
        print("wrong input enter again ")
     
while(True): 
    typee=input("which type calculator")
    calculator(typee)