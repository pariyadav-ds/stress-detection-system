import mysql.connector as ms
conn=ms.connect(host="localhost", user="root", password="sony", database="stress_detection")
curl=conn.cursor()
if conn.is_connected():
    print("connected")
else:
    print("not connected")

def create_userrecord():
   query_user="""create table userrecord
    (user_id varchar(10) NOT NULL PRIMARY KEY,
     uname varchar(50),
     uage int,
     ugender varchar(30),
     uoccupation varchar(50)
     )"""
   curl.execute(query_user)
   print("Table user created")

def create_activity_data():
    query_activity_data="""create table activity_data
    (activity_id varchar(10) NOT NULL PRIMARY KEY,
     sleep_hours int,
     heart_rate varchar(10),
     screen_time int
     )"""
    curl.execute(query_activity_data)
    print("table activity_data created")

def create_stress_analyst():
    query_stress_analyst="""create table stress_analyst
    (analyst_id varchar(10) NOT NULL PRIMARY KEY,
     user_id varchar(10),
     activity_id varchar(10),
     stress_level varchar(30),
     suggestion varchar(100)
     )"""
    curl.execute(query_stress_analyst)
    print("table stress_analyst created")

create_stress_analyst()
create_activity_data()
create_userrecord()
