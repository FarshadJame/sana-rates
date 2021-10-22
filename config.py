import mysql.connector

URL = 'https://api.tgju.online/v1/data/sana/json'

DB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sana")

# save in mysql
FLAG = False
