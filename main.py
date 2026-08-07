import sys
import json
import os
import shutil


def load_entries():  # Загружает JSON данные
    if os.path.exists("main_json.json"):
        with open("main_json.json", "r") as f:
            try:
                data = json.load(f)
                return data
            except:
                if os.path.exists("backup_json.json"):
                    with open("backup_json.json", "r") as f:
                        try:
                            data = json.load(f)
                            return data
                        except:
                            return []
                else:
                    return []
    else:
        if os.path.exists("backup_json.json"):
            with open("backup_json.json", "r") as f:
                try:
                    data = json.load(f)
                    return data
                except:
                    return []
        else:
            return []
def save_entries(entries):
    with open("temp_json.json", "w") as f:
        json.dump(entries, f)
    try:
        with open("temp_json.json", "r") as f:
            json.load(f)
        os.replace("temp_json.json", "main_json.json")
        shutil.copy("main_json.json", "backup_json.json")
    except json.JSONDecodeError:
        if os.path.exists("temp_json.json"):
            os.remove("temp_json.json")
def count_entries(entries):  # Счетчик count
    if entries == []:
        return 0
    numbers = []
    for i in entries:
        numbers.append(i["number"])
    maximum = max(numbers)
    return maximum

entries = load_entries()
count_result = count_entries(entries)

def menu():
    print(
        " 1.Новая запись \n 2.Посмотреть записи \n 3.Найти запись \n 4.Редактирование записи \n 5.Удалить запись \n 6.Выход")
def info_day(number, data, learning, timelearning, kpd):
    print("\033[35m=================================\033[0m", "\nID:", number, "\nДата:", data, "\nЧто изучал сегодня:",
          learning, "\nВремя:", timelearning, "\nОценка дня:", kpd,
          "\n\033[35m=================================\033[0m")
def appentry(entries):
    entry = {
        "number": number,
        "data": data,
        "learning": learning,
        "time": timelearning,
        "kpd": kpd
    }
    entries.append(entry)
def input_validation(value): #Проверка пустых полей
    while value == "":
           value = input("\033[31mВы ничего не ввели, введите пожалуйста данные.\033[0m")
    return value
def editing(change,i): #Редактирование
    if change == 1:
        change_data = input_validation(input("Введите новое значение: "))
        i["data"] = change_data
    elif change == 2:
        change_learning = input_validation(input("Введите новое значение: "))
        i["learning"] = change_learning
    elif change == 3:
        change_time = input_validation(input("Введите новое значение: "))
        i["time"] = change_time
    elif change == 4:
        change_kpd = input_validation(input("Введите новое значение: "))
        i["kpd"] = change_kpd
    return i

while True:
    menu()
    answer = int(input("Выберете пункт:"))
    if answer == 1:  # 1.Новая запись
        count_result += 1
        number = count_result
        data = input_validation(input("Дата: "))
        learning = input_validation(input("Что изучал сегодня? "))
        timelearning = input_validation(input("Сколько времени занимался?(В минутах) "))
        kpd = input_validation(input("Какая оценка дня? "))
        appentry(entries)
        info_day(number, data, learning, timelearning, kpd)
        save_entries(entries)
    elif answer == 2:  # 2.Посмотреть записи
        if len(entries) == 0:
            print("\033[31mЗаписей не найдено😰\033[0m")
        for i in entries:
            info_day(i["number"], i["data"], i["learning"], i["time"], i["kpd"])
    elif answer == 3:  # 3.Найти запись
        search = int(input("Введите номер ID:"))
        found = False
        for i in entries:
            if i["number"] == search:
                found = True
                info_day(i["number"], i["data"], i["learning"], i["time"], i["kpd"])
        if found == False:
            print("\033[31mЗапись не найдена😰\033[0m")
    elif answer == 4:  # 4.Редактирование записи
        id_search = int(input("Введите ID"))
        found = False
        for i in entries:
            if i["number"] == id_search:
                found = True
                info_day(i["number"], i["data"], i["learning"], i["time"], i["kpd"])
                change = int(input("Что хотите изменить? \n1.Дата \n2.Что изучал \n3.Время изучения \n4.Оценка дня"))
                editing(change, i)
                info_day(i["number"], i["data"], i["learning"], i["time"], i["kpd"])
                print("\033[32mДанные обновлены!\033[0m")
                save_entries(entries)
                break
        if found == False:
            print("\033[31mЗапись не найдена😰\033[0m")
    elif answer == 5:  # 5.Удалить запись
        id_search = int(input("Введите ID записи которую хотите удалить."))
        found = False
        for i in entries:
            if i["number"] == id_search:
                found = True
                info_day(i["number"], i["data"], i["learning"], i["time"], i["kpd"])
                confirmation = int(input("Подтвердите удаление 1(Да), 2(Нет)"))
                if confirmation == 1:
                    entries.remove(i)
                    print("\033[32mЗапись удалена!\033[0m")
                    save_entries(entries)
                    break
                elif confirmation == 2:
                    print("\033[31mУдаление прервано!\033[0m")
        if found == False:
            print("\033[31mЗапись не найдена😰\033[0m")
    elif answer == 6:  # 6.Выход
        save_entries(entries)
        print("\033[32mДо скорых встреч!\033[0m👋👋👋")
        sys.exit(1)

# 123
