import mysql.connector as ms

cnx = ms.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="stress_detection"
)

def add_activity_data():
    cursor = cnx.cursor()
    activity_id = input("Enter activity id: ")
    sleep_hours = int(input("Enter sleep hours: "))
    heart_rate = input("Enter heart rate: ")
    screen_time = int(input("Enter screen time: "))

    query = """
    INSERT INTO activity_data
    (activity_id, sleep_hours, heart_rate, screen_time)
    VALUES (%s, %s, %s, %s)
    """
    values = (activity_id, sleep_hours, heart_rate, screen_time)

    cursor.execute(query, values)
    cnx.commit()
    cursor.close()
    print("RECORD INSERTED IN ACTIVITY TABLE")


def display_activity_data():
    cursor = cnx.cursor()
    print("Displaying data from activity table")
    cursor.execute("SELECT * FROM activity_data")
    record=cursor.fetchall()
    for row in record:
        print("records of the data is as follow")
        print("Activty id=", row[0])
        print("Sleep hours=", row[1])
        print("Heart rate=", row[2])
        print("Screen time=", row[3])
        
    cursor.close()


def search_activity_data(aid):
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM activity_data WHERE activity_id = %s", (aid,))

    records = cursor.fetchall()
    print("ACTIVITY DATA REPORT")
    for row in records:
        print("ActivityID:", row[0])
        print("Sleep Hours:", row[1])
        print("Heart Rate:", row[2])
        print("Screen Time:", row[3])
    cursor.close()


def update_activity_data(aid):
    cursor = cnx.cursor()
    new_sleep = int(input("Enter new sleep hours: "))

    query = """
    UPDATE activity_data
    SET sleep_hours = %s
    WHERE activity_id = %s
    """

    cursor.execute(query, (new_sleep, aid))
    cnx.commit()

    if cursor.rowcount > 0:
        print("Record updated")
    else:
        print("Record not found")

    cursor.close()


def delete_activity_data(aid):
    cursor = cnx.cursor()

    cursor.execute(
        "DELETE FROM activity_data WHERE activity_id = %s", (aid,)
    )
    cnx.commit()

    if cursor.rowcount > 0:
        print("Record deleted")
    else:
        print("Record not found")

    cursor.close()
