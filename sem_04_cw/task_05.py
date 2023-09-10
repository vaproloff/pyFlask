# Задание No5.
# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории
# и выводить результаты в консоль.
# Используйте процессы.

import os
import multiprocessing

PATH = '../lec_04'
counter = multiprocessing.Value('i', 0)


def count_words(filename: str, count) -> None:
    with open(filename, 'r', encoding='utf-8') as f:
        words_count = len(f.read().split())
        print(f'{filename}: {words_count}')
        with count.get_lock():
            count.value += words_count


if __name__ == '__main__':
    processes = []
    for root, dirs, files in os.walk(PATH):
        for file in files:
            file_path = os.path.join(root, file)
            process = multiprocessing.Process(target=count_words, args=(file_path, counter))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

    print(f'Total: {counter.value}')



