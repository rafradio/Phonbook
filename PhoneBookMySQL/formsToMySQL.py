import mysql.connector
from numpy import append
import pandas as pd

class FormToMSQLQuery:
    def __init__(self, passwordMySQL):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password=passwordMySQL,
            database="database3"
        )
        self.mycursor = self.mydb.cursor()

    def FormMySQLInsert(self, dataSQL):
        sql = "INSERT INTO database3.phone_book (FirstName, LastName, Telephone, Mail) VALUES (%s, %s, %s, %s)"
        self.val = dataSQL
        self.mycursor.execute(sql, self.val)

        self.mydb.commit()

    def MySQLToFile(self, query):
        sql = query
        self.mycursor.execute(sql)
        myAllData = self.mycursor.fetchall()
      
        columnNames = {"id": [], "FirstName" : [], "LastName": [], "Telephone": [], "Mail" : []}
        counter = 0
        for i in columnNames.keys(): 
            for x in myAllData: columnNames[i].append(x[counter])
            counter += 1
        df = pd.DataFrame(columnNames)
        df_csv = df.to_csv("phonebook.csv", sep=";")
