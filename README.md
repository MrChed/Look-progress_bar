# DEMO Look-progress_bar

**Version:** demo v1.0

### Описание

Look-progress_bar - это прогресс-бар, который выведет процесс загрузки новых библиотек. Я создал свою собственную библиотеку, которая позволяет загружать библиотеки на новом уровне! (Python)

Возможно, я сделал что-то, что не требовалось, но я сделал это с любовью к проекту.

# Введите название библиотеки и ждите!

## Пример использования

```python
Введите название библиотеки, которую вы хотите скачать: telebot
```

### Результат:
```
Requirement already satisfied: telebot in c:\users\user\pycharmprojects\dsod\gptchat\lib\site-packages (0.0.5)
Requirement already satisfied: pyTelegramBotAPI in c:\users\user\pycharmprojects\dsod\gptchat\lib\site-packages (from telebot) (4.14.0)
Requirement already satisfied: requests in c:\users\user\pycharmprojects\dsod\gptchat\lib\site-packages (from telebot) (2.31.0)
Requirement already satisfied: certifi>=2017.4.17 in c:\users\user\pycharmprojects\dsod\gptchat\lib\site-packages (from requests->telebot) (2023.7.22)
Requirement already satisfied: urllib3<3,>=1.21.1 in c:\users\user\pycharmprojects\dsod\gptchat\lib\site-packages (from requests->telebot) (2.1.0)
Requirement already satisfied: charset-normalizer<4,>=2 in c:\users\user\pycharmprojects\dsod\gptchat\lib\site-packages (from requests->telebot) (3.3.2)
Requirement already satisfied: idna<4,>=2.5 in c:\users\user\pycharmprojects\dsod\gptchat\lib\site-packages (from requests->telebot) (3.4)

[notice] A new release of pip available: 22.3.1 -> 23.3.1
[notice] To update, run: python.exe -m pip install --upgrade pip
Библиотека 'telebot' успешно установлена
Загрузка файла 'telebot-0.0.5-py3-none-any.whl'...
Progress: |██████████████████████████████████████████████████| 100.0% Complete
Файл 'telebot-0.0.5-py3-none-any.whl' успешно загружен
```

## Пример ошибок

```python
Введите название библиотеки, которую вы хотите скачать: ossswd
```

### Результат:
```
ERROR: Could not find a version that satisfies the requirement ossswd (from versions: none)
ERROR: No matching distribution found for ossswd

[notice] A new release of pip available: 22.3.1 -> 23.3.1
[notice] To update, run: python.exe -m pip install --upgrade pip
Ошибка при установке библиотеки 'ossswd': Command '['pip', 'install', 'ossswd']' returned non-zero exit status 1.
```

##Код

Ниже представлен код для реализации функциональности прогресс-бара при установке библиотек с использованием Python.

```python
import subprocess
import sys
import time

def download_library(library_name):
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'install', library_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            print(f"Библиотека '{library_name}' успешно установлена")
            print(f"Загрузка файла '{library_name}.whl'...")
            show_progress_bar()
            print(f"Файл '{library_name}.whl' успешно загружен")
        else:
            print(f"Ошибка при установке библиотеки '{library_name}': {result.stderr}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def show_progress_bar():
    for i in range(101):
        time.sleep(0.05)  # имитация процесса загрузки
        sys.stdout.write(f"\rProgress: |{'█' * i}{' ' * (100 - i)}| {i}% Complete")
        sys.stdout.flush()

if __name__ == '__main__':
    library_name = input("Введите название библиотеки, которую вы хотите скачать: ")
    download_library(library_name)
```

Этот код позволяет:
1. Ввести название библиотеки для скачивания.
2. Установить библиотеку с помощью pip.
3. Показать прогресс-бар в консоли, имитирующий процесс загрузки.

Теперь вы можете легко скачать нужные библиотеки и наблюдать за процессом установки в реальном времени.
