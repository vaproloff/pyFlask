# Задание No4.
# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории
# и выводить результаты в консоль.
# Используйте потоки.

import os
import threading

PATH = '../lec_04'
count = 0


def count_words(filename: str) -> None:
    global count
    with open(filename, 'r', encoding='utf-8') as f:
        words_count = len(f.read().split())
        print(f'{filename}: {words_count}')
        count += words_count


if __name__ == '__main__':
    threads = []
    for root, dirs, files in os.walk(PATH):
        for file in files:
            file_path = os.path.join(root, file)
            thread = threading.Thread(target=count_words, args=[file_path, ])
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    print(f'Total: {count}')



