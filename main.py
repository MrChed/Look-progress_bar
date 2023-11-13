import time
import sys
import requests
import subprocess


def search_library(library_name):
    # Запрос к PyPI API для поиска библиотеки
    response = requests.get(f"https://pypi.org/pypi/{library_name}/json")

    # Проверка успешности запроса
    if response.status_code == 200:
        # Извлечение информации о библиотеке из ответа
        library_info = response.json()
        return library_info
    else:
        # В случае ошибки возвращаем None или более подходящее значение
        return None


class ProgressBar:
    def __init__(self, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.length = length
        self.fill = fill
        self.start_time = time.time()
        self.last_update = self.start_time
        self.update_interval = 0

    def update(self, count):
        percent = ("{0:." + str(self.decimals) + "f}").format(100 * (count / float(self.total)))
        filled_length = int(self.length * count // self.total)
        bar = self.fill * filled_length + '-' * (self.length - filled_length)
        sys.stdout.write('\r%s |%s| %s%% %s' % (self.prefix, bar, percent, self.suffix))
        sys.stdout.flush()

    def finish(self):
        sys.stdout.write('\n')

    def start(self):
        self.update(0)

    def increment(self, count=1):
        current_time = time.time()
        if current_time - self.last_update >= self.update_interval:
            self.update(count)
            self.last_update = current_time

    def elapsed_time(self):
        return time.time() - self.start_time

class DownloadError(Exception):
    pass

def download_file(file_url, save_path, progress):
    response = requests.get(file_url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    if response.status_code == 404:
        raise DownloadError("File not found", 1001)

    progress.total = total_size
    progress.start()

    with open(save_path, 'wb') as file:
        downloaded_size = 0
        for data in response.iter_content(chunk_size=1024):
            file.write(data)
            downloaded_size += len(data)
            progress.increment(downloaded_size)

    progress.finish()
    return True

def download_library(library_name):
    try:
        subprocess.check_call(["pip", "install", library_name])
        print(f"Библиотека '{library_name}' успешно установлена")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при установке библиотеки '{library_name}': {e}")
    else:
        library_info = search_library(library_name)
        if library_info:
            file_url = library_info['urls'][0]['url']
            file_name = file_url.split('/')[-1]
            save_path = f"./{file_name}"
            print(f"Загрузка файла '{file_name}'...")

            progress = ProgressBar(0, prefix='Progress:', suffix='Complete', length=50, fill='█')
            download_file(file_url, save_path, progress)

            print(f"Файл '{file_name}' успешно загружен")
        else:
            print(f"Библиотека '{library_name}' не найдена")

if __name__ == "__main__":
    library_name = input("Введите название библиотеки, которую вы хотите скачать: ")

    download_library(library_name)
