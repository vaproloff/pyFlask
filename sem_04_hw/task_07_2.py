# Задание No7 (МНОГОПРОЦЕССОРНОСТЬ).
# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...].
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# В каждом решении нужно вывести время выполнения вычислений.

import multiprocessing
import time
from random import randint

MIN_NUM = 1
MAX_NUM = 100
NUM_QTY = 1_000_000

my_lst = [randint(MIN_NUM, MAX_NUM) for _ in range(NUM_QTY)]
total = multiprocessing.Value('i', 0)


def add_number(num: int, total_sum: multiprocessing.Value) -> None:
    with total_sum.get_lock():
        total_sum.value += num


if __name__ == '__main__':
    processes = []
    start_time = time.time()

    for item in my_lst:
        process = multiprocessing.Process(target=add_number, args=(item, total))
        processes.append(process)
        process.start()

        for process in processes:
            process.join()

    print(f'Total sum time (multiprocessing): {time.time() - start_time:.1f} sec')
    print(f'Total sum (multiprocessing): {total.value}')
    print(f'Total sum (for check): {sum(my_lst)}')
