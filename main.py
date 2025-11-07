def server_module(text, substring):
    if substring == "":
        return 0
    count = 0
    start = 0
    while True:
        index = text.find(substring, start)
        if index == -1:
            break
        count += 1
        start = index + 1
    return count

def user_module():
    print("=== Подсчёт количества вхождений строки ===")
    text = input("Введите первую строку: ").strip()
    substring = input("Введите подстроку для поиска: ").strip()
    if text == "":
        print("Ошибка: первая строка не может быть пустой.")
        return
    if substring == "":
        print("Ошибка: подстрока не может быть пустой.")
        return
    if text == substring:
        print("Строки совпадают.")
    result = server_module(text, substring)
    print(f"Количество вхождений: {result}")


user_module()
