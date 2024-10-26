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
