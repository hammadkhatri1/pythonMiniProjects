library_management=[]

while True:
    print ("   ####  LIBRARY MANAGEMENT SYSTEM  #### ")
    dec=int(input(" 1: to ADD\n 2: to VIEW \n 3: To DELETE\n 4: UPDATE\n  0: EXIT\n your decision:  "))
    if(dec==1):    
        #addition(id_list,name_list,grade_list)
        isbn=input("Enter isbn:  ")
        title=input("Enter title:  ")
        DOI=input("Enter doi:  ")
        info=(isbn," | ",title," | ",DOI,"\n")
        library_management.append(info)
    elif(dec==2):
        for item in library_management:
            print (" ".join(item))

    elif(dec==0):
        exit()