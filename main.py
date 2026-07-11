import sys
import json
import os


def load_entries():  # Загружает JSON данные
    if os.path.exists("test.json"):
        with open("test.json", "r") as f:
            data = json.load(f)
            return data
    else:
        return []


def save_entries(entries):  # сохраняет данные в JSON
    with open("test.json", "w") as f:
        json.dump(entries, f)


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


while True:
    menu()
    answer = int(input("Выберете пункт:"))
    if answer == 1:  # 1.Новая запись
        count_result += 1
        number = count_result
        data = input("Дата")
        while data == "":
            if data == "":
                data = input("\033[31mВы ничего не ввели, введите пожалуйста данные.\033[0m")
        learning = input("Что изучал сегодня?")
        while learning == "":
            if learning == "":
                learning = input("\033[31mВы ничего не ввели, введите пожалуйста данные.\033[0m")
        timelearning = input("Сколько времени занимался?(В минутах)")
        while timelearning == "":
            if timelearning == "":
                timelearning = input("\033[31mВы ничего не ввели, введите пожалуйста данные.\033[0m")
        kpd = input("Какая оценка дня?")
        while kpd == "":
            if kpd == "":
                kpd = input("\033[31mВы ничего не ввели, введите пожалуйста данные.\033[0m")
        entry = {
            "number": number,
            "data": data,
            "learning": learning,
            "time": timelearning,
            "kpd": kpd
        }
        entries.append(entry)
        info_day(number, data, learning, timelearning, kpd)
        save_entries(entries)
    elif answer == 2:  # 2.Посмотреть записи
        if len(entries) == 0:
            print("Записей не найдено")
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
                if change == 1:
                    change_data = input("Введите новое значение")
                    i["data"] = change_data
                    info_day(i["number"], i["data"], i["learning"], i["time"], i["kpd"])
                    print("\033[32mДанные обновлены!\033[0m")
                    save_entries(entries)
                elif change == 2:
                    change_learning = input("Введите новое значение")
                    i["learning"] = change_learning
                    info_day(i["number"], i["data"], i["learning"], i["time"], i["kpd"])
                    print("\033[32mДанные обновлены!\033[0m")
                    save_entries(entries)
                    break
                elif change == 3:
                    change_time = input("Введите новое значение")
                    i["time"] = change_time
                    info_day(i["number"], i["data"], i["learning"], i["time"], i["kpd"])
                    print("\033[32mДанные обновлены!\033[0m")
                    save_entries(entries)
                    break
                elif change == 4:
                    change_kpd = input("Введите новое значение")
                    i["kpd"] = change_kpd
                    info_day(i["number"], i["data"], i["learning"], i["time"], i["kpd"])
                    print("\033[32mДанные обновлены!\033[0m")
                    save_entries(entries)
        if found == False:
            save_entries(entries)
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
                    save_entries(entries)
        if found == False:
            save_entries(entries)
            print("\033[31mЗапись не найдена😰\033[0m")
    elif answer == 6:  # 6.Выход
        save_entries(entries)
        sys.exit(1)

# 123
