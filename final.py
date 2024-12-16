from datetime import datetime
#Создаем словарь note
note = {}
note["username"] = input ("Введите имя пользователя: ")

# Создаем список заголовков заметки
note["titles"] = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    note["titles"].append(title)

note["content"] = input ("Введите описание заметки: ")
note["status"] = input ("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
temp_created_date = input ("Введите дату создания заметки в формате день.месяц.год: ")
form_created_date = datetime.strptime (temp_created_date, "%d.%m.%Y")
note["created_date"] = datetime.strftime ( form_created_date, "%d.%m")
temp_issue_date = input ("Введите дату истечения заметки в формате день.месяц.год: ")
form_issue_date = datetime.strptime (temp_issue_date, "%d.%m.%Y")
note["issue_date"] = datetime.strftime( form_issue_date,"%d.%m")


print("\nСобранная информация о заметке:")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")
