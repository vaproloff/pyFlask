# Задание No2
# Написать программу, которая считывает список из 10 URL- адресов и одновременно загружает данные с каждого адреса.
# После загрузки данных нужно записать их в отдельные файлы.
# Используйте процессы.

import requests
from multiprocessing import Process
import time

urls = [
    'http://vk.com/',
    'https://youtube.com/',
    'https://wireframe.cc/WJ4Lb1',
    'https://letsencrypt.org/ru/',
    'https://getbootstrap.com/docs/5.3/components/button-group/',
    'https://edit.org/edit/all/14sxb7zt9',
    'https://pythontutor.com/render.html#mode=edit',
    'https://timeweb.cloud/',
    'https://linkmeup.ru/blog/',
    'https://ya.ru'
]


def download(url):
    response = requests.get(url)
    filename = 'multiprocessing_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time() - start_time:.2f}seconds")


processes = []
start_time = time.time()


if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
