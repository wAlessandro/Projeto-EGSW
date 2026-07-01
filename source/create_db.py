import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@bost4fedid4$",
    )

cursor = connection.cursor()

cursor.execute("CREATE DATABASE if NOT EXISTS ong_animais")