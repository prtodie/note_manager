from datetime import datetime

username = input ("Введите имя пользователя: ") #Ввод данных
title = input ("Введите заголовок заметки: ")
content = input ("Введите описание заметки: ")
status = input ("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
temp_created_date = input ("Введите дату создания заметки в формате день.месяц.год: ")
form_created_date = datetime.strptime (temp_created_date, "%d.%m.%Y")
created_date = datetime.strftime ( form_created_date, "%d.%m") #Преобразование даты в нужный формат для вывода
temp_issue_date = input ("Введите дату истечения заметки в формате день.месяц.год: ")
form_issue_date = datetime.strptime (temp_issue_date, "%d.%m.%Y")
issue_date = datetime.strftime( form_issue_date,"%d.%m")


print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", issue_date) #Вывод данных
