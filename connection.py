import mysql.connector

try:
        def connect_to_db():
            return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="medical_center"
        )
        print("Успешное подключение!")
except:
    print("Ошибка!")
