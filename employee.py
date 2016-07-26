import mysql.connector


def menu():
    print (" **** MENU ***")
    print ("1: Add")
    print ("2: View")
    print ("3: Delete")
    print ("4: update")
    print ("5: Search")
    print ("  0: EXIT")

       
def addition():
    try:
        cnx = mysql.connector.connect(user='root', password='dell',host='127.0.0.1',database='study')
        name=input("Enter Name:  ")
        gender=input("Enter gender:  ")
        sql="insert into emp(Name,Gender) values ('%s', '%s' )" %(name,gender)
        cursor=cnx.cursor()
        cursor.execute(sql)
        cnx.commit()
        cnx.close()
    except Exception as e:
        db.rollback()
        print (e)
    else:
        print ("Record Added Successfully")
        

def view():
    try:
        cnx = mysql.connector.connect(user='root', password='dell',host='127.0.0.1',database='study')
        cursor=cnx.cursor()
        sql="select * from emp"
        cursor.execute(sql)
        results=cursor.fetchall()
        print ("====================")
        for row in results:
            id=row[0]
            name=row[1]
            gender=row[2]
            print ("-------------")
            print ("id: %d \nName: %s \nGender: %s" % (id,name,gender))
        print ("-------------")
        print ("====================")
        cnx.close()
    except Exception as e:
        print (e)

def up():
    cnx = mysql.connector.connect(user='root', password='dell',host='127.0.0.1',database='study')
    name=input("Enter Name:  ")
    gender=input("Enter gender:  ")
    id=int(input("Enter I:  "))
        
    sql = "UPDATE emp SET Name = '%s' , Gender ='%s' WHERE id = %d"%(name,gender,id)
    cursor=cnx.cursor()
        
    cursor.execute(sql)
    cnx.commit()
    cnx.close()

def delete():
    try:
        db = mysql.connector.connect(user='root', password='dell',host='127.0.0.1',database='study')
        id=int(input("Enter id:  "))
        sql="delete from emp where id=%d"%(id)
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()

    except Exception as e:
        print (e)
    else:
        print("Record deleted successfully")

def search():
    db = mysql.connector.connect(user='root', password='dell',host='127.0.0.1',database='study')
    id=int(input("Enter id:  "))
    sql="Select * from emp where id=%d"%(id)
    cursor = db.cursor()
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        id=row[0]
        name=row[1]
        gender=row[2]
        print ("-------------")
        print ("id: "+str(id)+"\nName: "+name+"\nGender: "+gender+"\n")
    print ("-------------")
    db.close()
    

while (True):
    print ("  ### EMPLOYEE MANAGEMENT SYSTEM ### ")
    menu()
    dec=int(input("Enter value: "))
    if(dec==1):
        addition()
    elif(dec==2):
        view()
    elif(dec==3):
        delete()
    elif(dec==4):
        up()
    elif(dec==5):
        search()
    elif(dec==0):
        exit()
    
        
            
    
