# Задание No7 (МНОГОПОТОЧНОСТЬ).
# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...].
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# В каждом решении нужно вывести время выполнения вычислений.

import threading
import time
from random import randint

MIN_NUM = 1
MAX_NUM = 100
NUM_QTY = 1_000_000

my_lst = [randint(MIN_NUM, MAX_NUM) for _ in range(NUM_QTY)]
total = 0


def add_number(num: int) -> None:
    global total
    total += num


if __name__ == '__main__':
    threads = []
    start_time = time.time()

    for item in my_lst:
        thread = threading.Thread(target=add_number, args=[item, ])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Total sum time (threading): {time.time() - start_time:.1f} sec')
    print(f'Total sum (threading): {total}')
    print(f'Total sum (for check): {sum(my_lst)}')
