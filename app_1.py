# Напишите функцию, которая принимает на вход строку -
# абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов:
# путь, имя файла, расширение файла.
# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
# Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')


def split_path(text):
    """Function returns a tuple of elements: path, file name, file extension."""
    parts = text.split('/')
    path = '/'.join(parts[:-1])
    file_name, file_extension = parts[-1].split('.')
    result = (path + '/', file_name, '.' + file_extension)
    return result


input_path = "c:/Users/Vladislav/Desktop/deep_to_python/test.txt"
output_tuple = split_path(input_path)
print(output_tuple)
