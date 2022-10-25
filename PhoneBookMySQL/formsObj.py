from tkinter import * 
import formsToMySQL

class FormObjects:
    def __init__(self, name, size, passwordMySQL = ""):
        self.form = Tk()
        self.form.title(name)
        self.form.geometry(size)
        self.infoEntry = {}
        self.data = {}
        self.passwordMySQL = passwordMySQL
        
    def close(self):
        self.form.destroy()
        self.form.quit()

    def Actions(self):
        self.form.protocol('WM_DELETE_WINDOW', self.close)
        self.form.mainloop()

    def ButtonCreate(self, objTk, buttonAction, button_name, position):
        self.button = Button(objTk, text=button_name, command=buttonAction, width=30, height=3, bg="#d8c5c5")
        self.button.grid(row=position[0], column=position[1], padx=15, pady=15)

    def TextEntry(self, objTk, textName, position, i, flag = 0):
        print(type(objTk))
        self.infoLabel = Label(objTk, text=textName)
        if flag == 0: self.infoEntry[i] = Entry(objTk, width=30)
        else: 
            password = StringVar()
            self.infoEntry[i] = Entry(objTk, width=30, textvariable=password, show="*")
            
        self.infoLabel.grid(row=position[0], column=position[1], padx=15, pady=15)
        self.infoEntry[i].grid(row=position[0], column=position[1] + 1, padx=15, pady=15)

    def ButtonTextForm(self, objTk):
        self.btnTextForm = Button(objTk, text="Запишите данные", command = self.btnDataSave)
        self.btnTextForm.grid(columnspan=2, padx=15, pady=15)

    def btnDataSave(self):
        # stringText = ";".join([self.infoEntry[i].get() for i in range(len(self.infoEntry))])
        # stringText += "\n"
        # print(stringText)
        # with open ("phoneBook.csv", 'a', encoding = 'utf-8') as data:
        #     data.write(stringText)
        dataSQL = tuple([self.infoEntry[i].get() for i in range(len(self.infoEntry))])
        mySqlSent = formsToMySQL.FormToMSQLQuery(self.passwordMySQL)
        mySqlSent.FormMySQLInsert(dataSQL)

    def button_clicked_1(self):
        self.passwordMySQL = self.infoEntry[0].get()
        db = formsToMySQL.FormToMSQLQuery(self.passwordMySQL)
        db.MySQLToFile("SELECT * FROM database3.phone_book;")

      