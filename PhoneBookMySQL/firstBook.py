from tkinter import * 
import formsObj
import buttonActions

def button_clicked():
    passwordMySQL = form1.infoEntry[0].get()
    grid = [(0, 0), (0, 2), (1, 0), (1, 2)]
    fieldNames = ["Имя", "Фамилия", "Телефон", "Почта"]
    form2 = formsObj.FormObjects("Вводим данные", "800x600", passwordMySQL)
    for i in range(4): form2.TextEntry(form2.form, fieldNames[i], grid[i], i)
    form2.ButtonTextForm(form2.form)
    form2.Actions()



form1 = formsObj.FormObjects("Моя телефонная книжка", "600x200")
form1.ButtonCreate(form1.form, button_clicked, "Вводим данные", (0, 0))
form1.ButtonCreate(form1.form, form1.button_clicked_1, "Записываем в файл", (0, 1))
form1.TextEntry(form1.form, "Пароль в MySQL", (1, 0), 0, 1)
form1.Actions()