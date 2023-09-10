# Задание No3
# Написать программу, которая считывает список из 10 URL- адресов и одновременно загружает данные с каждого адреса.
# После загрузки данных нужно записать их в отдельные файлы.
# Используйте асинхронный подход.

import asyncio
import aiohttp
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


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = 'asyncio_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            with open(filename, "w", encoding='utf-8') as f:
                f.write(text)
            print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()

if __name__ == '__main__':
    asyncio.run(main())
