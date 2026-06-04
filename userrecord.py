import mysql.connector as ms
cnx=ms.connect(host="localhost", user="root", passwd="1234", db="stress_detection")

def add_user_data():
    cursor=cnx.cursor()
    myuser_id=input("Enter user id")
    myuname=input("Enter user name")
    myuage=int(input("Enter age"))
    myugender=input("Enter gender")
    myuoccupation=input("Enter the occupation")
    query="insert into userrecord(user_id, uname, uage, ugender, uoccupation) VALUES(%s,%s, %s, %s,%s)"
    values=(myuser_id, myuname, myuage, myugender, myuoccupation)

    cursor.execute(query,values)
    cnx.commit()
    cursor.close()
    print("RECORD INSERTED")

def display_userrecord_data():
    cursor=cnx.cursor()
    query=("select * from userrecord")
    cursor.execute(query)
    record=cursor.fetchall()
    for row in record:
        print("User id=", row[0])
        print("User name=", row[1])
        print("User age=", row[2])
        print("User gender=", row[3])
        print("User occupation=", row[4])
        print("Data Displayed")
        print()
    cursor.close()

def search_userrecord_by_name(myuname):
    cursor=cnx.cursor()
    query="select * from userrecord where uname=%s"
    cursor.execute(query,(myuname,))    
    record=cursor.fetchall()
    for row in record:
        print("Records of the data is as follow")
        print("User id=", row[0])
        print("User name=", row[1])
        print("User age=", row[2])
        print("User gender=", row[3])
        print("User occupation=", row[4])
        print("Data Displayed")
    cursor.close()


def search_userrecord_by_id(uno):
    cursor=cnx.cursor()
    query="select * from userrecord where user_id= %s"
    cursor.execute(query,(uno,))    
    record=cursor.fetchall()
    for row in record:
        print("Records of the data is as follow")
        print("User id=", row[0])
        print("User name=", row[1])
        print("User age=", row[2])
        print("User gender=", row[3])
        print("User occupation=", row[4])
        print("Data Displayed")
    cursor.close()

def update_userrecord(myuname):
    cursor=cnx.cursor(buffered=True)
    cursor.execute("select * from userrecord where uname='%s' ")
    print("Enter the new data")
    age=int(input("Enter user age"))
    gender=input("Enter user gender")
    occu=input("Enter user occupation")
    cursor.execute("update userrecord set\
                   uage= %s, ugender= '%s', uoccupation='%s'\
                   where uname='%s'" %(age, gender, occu,myuname))
    cnx.commit()
    
    print("Record(s) updated successfully")
    cursor.close()

def user_delete(user_id):
    cursor=cnx.cursor()
    cursor.execute("select * from userrecord where user_id=%s" , (user_id,))
    record=cursor.fetchall()
    print("Displaying record for deletion")
    print(record)
    confirm=input("Do you want to delete the record")
    if confirm=="y":
        cursor.execute("delete from userrecord where user_id='%s' " %user_id)
        cnx.commit()
        print(cursor.rowcount, "records deleted succesfully")
    else:
        print("delete operation cancelled")
        cursor.close()
