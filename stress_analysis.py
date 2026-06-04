import mysql.connector as ms
cnx = ms.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="stress_detection"
)

def add_record_stress_analysis():
    cursor = cnx.cursor()
    analyst_id = input("Enter analyst id:")
    user_id = input("Enter user id: ")
    activity_id = input("Enter activity id: ")

    cursor.execute("SELECT sleep_hours, heart_rate, screen_time FROM activity_data \
                   WHERE activity_id=%s",(activity_id,))
    data = cursor.fetchone()      
    sleep, heart, screen = data

    if sleep < 6 or int(heart) > 90 or screen > 7:
        stress = "High"
        suggestion = "Sleep more & reduce screen time"
    elif sleep <= 7 or int(heart) >= 75 or screen >= 5:
        stress = "Medium"
        suggestion = "Reduce screen time"
    else:
        stress = "Low"
        suggestion = "Maintain healthy routine"

    query = """
    INSERT INTO stress_analyst
    (analyst_id, user_id, activity_id, stress_level, suggestion)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(query, (analyst_id, user_id, activity_id, stress, suggestion))
    cnx.commit()

    print("STRESS ANALYSIS RECORD INSERTED")
    cursor.close()


def display_record_stress_analysis():
    cursor = cnx.cursor()

    query = """
    SELECT u.user_id, u.uname,
           a.sleep_hours, a.heart_rate, a.screen_time,
           s.stress_level, s.suggestion
    FROM userrecord u
    JOIN stress_analyst s ON u.user_id = s.user_id
    JOIN activity_data a ON a.activity_id = s.activity_id
    """

    cursor.execute(query)
    records = cursor.fetchall()
    print("REPORT OF STRESS ANANLYSIS")

    for row in records:
        
        print("User ID:", row[0])
        print("Name:", row[1])
        print("Sleep Hours:", row[2])
        print("Heart Rate:", row[3])
        print("Screen Time (IN HOURS) :", row[4])
        print("Stress Level:", row[5])
        print("Suggestion:", row[6])
        print()

    cursor.close()        

def update_record_stress_analysis():
    cursor=cnx.cursor()

    activity_id=input("Enter activity id to update stress record:")
    new_stress=input("Enter new stress level (High/Medium/Low):")
    new_suggestion=input('Enter new suggestion:')

    query="""
    UPDATE stress_analyst
    SET stress_level=%s,
    suggestion=%s
    WHERE activity_id=%s
    """

    cursor.execute(query,(new_stress, new_suggestion, activity_id))
    cnx.commit()

    if cursor.rowcount>0:
        print("Stress analysis record updated successfully")
    else:
        print("No record found for given activity id:")

    cursor.close()

def delete_record_stress_analysis():
    cursor=cnx.cursor()

    activity_id=input('Enter activity id to delete stress record')

    query="DELETE FROM stress_analyst WHERE activity_id=%s"
    cursor.execute(query,(activity_id,))
    cnx.commit()

    if cursor.rowcount>0:
        print('stress analysis record deleted successfully')
    else:
        print('no record found for given activity id')

    cursor.close()    
                     
def search_by_activity_id(aid):
    cursor=cnx.cursor()
    cursor.execute('SELECT * FROM stress_analyst WHERE activity_id=%s',(aid,))
    records=cursor.fetchall()
    print("REPORT OF STRESS ANALYSIS")
    for row in records:
        print("AnalystID:", row[0])
        print("User ID:", row[1])
        print("Activity ID:", row[2])
        print("Stress:", row[3])
        print("Suggestion:",row[4])
    cursor.close()

def search_by_user_id(uid):   
    cursor=cnx.cursor()
    cursor.execute('SELECT * FROM stress_analyst WHERE user_id=%s',(uid,))
    records=cursor.fetchall()
    print("REPORT OF STRESS ANALYSIS")
    for row in records:
        print("AnalystID:", row[0])
        print("User ID:", row[1])
        print("Activity ID:", row[2])
        print("Stress:", row[3])
        print("Suggestion:",row[4])
    
    cursor.close()

def search_by_analyst_id(anid):
    cursor=cnx.cursor()
    cursor.execute('SELECT * FROM stress_analyst WHERE analyst_id=%s',(anid,))    
    records=cursor.fetchall()
    print("REPORT OF STRESS ANALYSIS")
    for row in records:
        print("AnalystID:", row[0])
        print("User ID:", row[1])
        print("Activity ID:", row[2])
        print("Stress:", row[3])
        print("Suggestion:",row[4])
    
    cursor.close()
