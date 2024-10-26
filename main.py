from file_operations import read_file, write_file, delete_last_lines, clear_file
from utils import get_user_input

def main():
    filename = 'example.txt'

    while True:
        action = get_user_input(
            "Введите 'r' для чтения файла, 'w' для записи, 'd' для удаления последних строк, "
            "'e' для изменения строки, 's' для поиска строки, "
            "'cl' для очистки файла, 'q' для выхода: "
        )

        if action == 'r':
            content = read_file(filename)
            print("Содержимое файла:")
            print(content)
        elif action == 'w':
            text = input("Введите текст для записи в файл: ")
            write_file(filename, text)
            print("Текст записан в файл.")
        elif action == 'd':
            num_lines = int(input("Сколько последних строк удалить? "))
            delete_last_lines(filename, num_lines)
            print(f"{num_lines} последняя(ие) строка(и) удалена(ы) из файла.")
        elif action == 'cl':
            result = clear_file(filename)
            print(result)
        elif action == 'q':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()