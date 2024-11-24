# Введение в потоки

from time import sleep
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
    """
    word_count - количество записываемых слов,
    file_name - название файла, куда будут записываться слова.
    """
    with open(file_name, 'w+', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово №  {i + 1}\n')
            sleep(0.1)
    print (f"Завершилась запись в файл {file_name}")

time_start1 = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end1 = datetime.now()
time_res1 = time_end1 - time_start1
print(f'Работа одним потоком: {time_res1}')

time_start2 = datetime.now()
thr_f5 = Thread(target=write_words, args=(10, "example5.txt"))
thr_f6 = Thread(target=write_words, args=(30, "example6.txt"))
thr_f7 = Thread(target=write_words, args=(200, "example7.txt"))
thr_f8 = Thread(target=write_words, args=(100, "example8.txt"))

thr_f5.start()
thr_f6.start()
thr_f7.start()
thr_f8.start()

thr_f5.join()
thr_f6.join()
thr_f7.join()
thr_f8.join()
time_end2 = datetime.now()
time_res2 = time_end2 - time_start2
print(f'Работа нескольких потоков: {time_res2}')