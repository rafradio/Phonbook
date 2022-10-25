import pandas as pd
import mysql.connector
import formsToMySQL

def button_clicked_1():
    db = formsToMySQL.FormToMSQLQuery()
    db.MySQLToFile("SELECT * FROM database3.phone_book;")