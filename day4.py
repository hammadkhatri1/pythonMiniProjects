garage={}



while True:
    dec=int(input("Enter value"))
    if(dec==1):
          model=input("Enter model:  ")
          name=input("Enter name:  ")
          garage[model]=name
    elif(dec==2):
        for x in garage:
            print (garage[x])
    elif(dec==0):
        exit()

