from connection import connect_to_db

def insert_schedule_data(schedule_data):
    conn = connect_to_db()
    cursor = conn.cursor()

    query = "INSERT INTO Schedule(DayOfWeek, StartTime, EndTime, BreakStartTime, BreakEndTime) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, schedule_data)

    conn.commit()
    cursor.close()
    conn.close()
