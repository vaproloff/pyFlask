# Задание No9 (МНОГОПОТОЧНОСТЬ).
# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Каждое изображение должно сохраняться в отдельном файле, название которого соответствует
#   названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# Программа должна выводить в консоль информацию о времени скачивания каждого изображения
#   и общем времени выполнения программы.

import argparse
import threading
import time
import requests
import os

img_urls = [
    'https://zastavok.net/main/priroda/1425294122.jpg',
    'https://i.pinimg.com/originals/1a/99/fe/1a99fe8ecdd4a3172ba084a256d5875e.jpg',
    'https://dingo.com.ua/source/roads/015.jpg',
    'https://i.pinimg.com/736x/61/9b/e3/619be348955a8ae6ef385fbcecf19029.jpg',
    'https://vocasia.id/blog/wp-content/uploads/2023/03/watermark-adalah-1-720x450.jpg'
]

IMG_DIR = 'images'


def download_image(url: str, target_dir: str) -> None:
    start_thread_time = time.time()
    response = requests.get(url)
    filename = url.split('/')[-1]
    with open(os.path.join(target_dir, filename), 'wb') as img:
        for data in response.iter_content(1024):
            img.write(data)
    print(f"Downloaded image {url} in {time.time() - start_thread_time:.2f} sec")


def parse():
    parser = argparse.ArgumentParser(description='Downloads images from given url list')
    parser.add_argument('-u', '--urls', nargs='+', type=str, help='Image URLs separated by space')
    return parser.parse_args()


if __name__ == '__main__':
    urls = parse().urls or img_urls

    if not os.path.exists(IMG_DIR):
        os.mkdir(IMG_DIR)

    start_time = time.time()

    threads = []
    for img_url in urls:
        thread = threading.Thread(target=download_image, args=[img_url, IMG_DIR])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Total download time (threading): {time.time() - start_time:.2f} sec')
