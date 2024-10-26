def read_file(filename):
    """Чтение содержимого текстового файла."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Файл не найден."

def write_file(filename, text):
    """Запись текста в текстовый файл."""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text + '\n')

def delete_last_lines(filename, num_lines=1):
    """Удаление последних строк из текстового файла."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Удаляем последние строки
        new_lines = lines[:-num_lines]

        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(new_lines)
    except FileNotFoundError:
        return "Файл не найден."