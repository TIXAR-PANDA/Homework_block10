# Многопроцессное программирование

import multiprocessing
from datetime import datetime
# Создайте функцию read_info(name)
def read_info(name):
    """name - название файла"""
    # Создали локальный список all_data
    all_data = []
    # Открыли файл name для чтения
    with open(name, 'r') as file1:
        while True:
            # Считываем информацию построчно
            line = file1.readline().strip()
            # добавляем каждую строку в список all_data
            all_data.append(line)
            # пока считанная строка не окажется пустой
            if not line:
                break

# Создайте список названий файлов в соответствии с названиями файлов архива
filenames = [f'./file {number}.txt' for number in range(1, 5)]
# filenames = ['./file 1.txt', './file 2.txt', './file 3.txt', './file 4.txt']

"""start1 = datetime.now()
# Вызовите функцию read_info для каждого файла по очереди:
for f in filenames:
    read_info(f)

end1 = datetime.now()
# вычислили время выполнения
time_of_line_function = end1 - start1
print(f'Время работы линейного вызова : {time_of_line_function}')"""

# Вызовите функцию read_info для каждого файла, используя многопроцессный подход
if __name__ == '__main__':
    start2 = datetime.now()# время начала работы

# многопроцессный подход: контекстный менеджер with и объект Pool
    with multiprocessing.Pool(processes=4) as pool:
        # Для вызова функции используйте метод map,
        # передав в него функцию read_info и список названий файлов
        pool.map(read_info, filenames)

    end2 = datetime.now()# время в конце работы
    # вычислили время выполнения
    time_of_multiprocessing = end2 - start2
    print(f'Время работы мультипроцесса : {time_of_multiprocessing}')
# Для избежания некорректного вывода запускайте линейный вызов и многопроцессный по отдельности,
# предварительно закомментировав другой.
