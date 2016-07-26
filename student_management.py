management=[]

def addition():    
    idStudent=int(input("Enter ID of student:  "))
    nameStudent=input("Enter name of student:  ")
    gradeStudent=input("Enter grade of student:  ")
    info=(idStudent," | ",nameStudent," | ",gradeStudent,"\n")
    management.append(info)

while(True):
    print ("    ^^^^Student Mangement System^^^^")
    dec=int(input("1: to add\n2: to view\n3: to delete\n4: to update\n  0: TO EXIT\nyour decision:  "))
    if(dec==1):
        addition()
      
    elif(dec==2):
        print ("ID     |      Name          | Grade")
        for item in management:
            print ("--------------------------")        
            print (" ".join(item))
        print ("--------------------------")
      
    elif(dec==0):
        exit()
    else:
        print ("Wrong input")



    