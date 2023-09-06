import requests
from multiprocessing import Process
import time

urls = ['https://t.me/python3k',
        'https://www.youtube.com/channel/UCQ1YbfMA6jeGamfA1RHMWHQ',
        'https://ya.ru/',
        'https://docs.python.org/3/library/asyncio.html',
        'https://habr.com/ru/articles/671602/',
        ]


def download(url):
    response = requests.get(url)
    filename = 'multiprocessing_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


processes = []
start_time = time.time()

if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
