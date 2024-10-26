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

def search_line(filename, search_text):
    """Поиск строки в текстовом файле."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        matches = [line for line in lines if search_text in line]
        return matches if matches else ["Совпадений не найдено."]
    except FileNotFoundError:
        return "Файл не найден."

def edit_line(filename, line_number, new_text):
    """Изменение строки в текстовом файле."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        if 0 < line_number <= len(lines):
            lines[line_number - 1] = new_text + '\n'  # Заменяем строку
            with open(filename, 'w', encoding='utf-8') as file:
                file.writelines(lines)
            return f"Строка {line_number} изменена."
        else:
            return "Номер строки вне диапазона."
    except FileNotFoundError:
        return "Файл не найден."