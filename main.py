from file_operations import read_file, write_file
from utils import get_user_input

def main():
    filename = 'example.txt'

    while True:
        action = get_user_input("Введите 'r' для чтения файла, 'w' для записи, 'q' для выхода: ")

        if action == 'r':
            content = read_file(filename)
            print("Содержимое файла:")
            print(content)
        elif action == 'w':
            text = input("Введите текст для записи в файл: ")
            write_file(filename, text)
            print("Текст записан в файл.")
        elif action == 'q':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()