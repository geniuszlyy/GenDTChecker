# GenDTChecker
 is a Python tool for validating Discord tokens. It checks the validity of a token and retrieves associated user information such as username, email, ID, and more. The tool is easy to use with a command-line interface and color-coded output.

# EN
**GenDTChecker(Gen Discord Token Checker)** - is a Python-based tool designed to check the validity of Discord tokens. It allows you to verify if a token is active and retrieve user information associated with it. The tool is designed for ease of use, providing a simple command-line interface with colored output for clarity.

## Features
- **Token Validation**: Check if a Discord token is valid and active.
- **User Information Retrieval**: Get details like username, email, ID, phone status, and avatar URL.
- **Data Saving**: Save retrieved user information to a file for future reference.

## Requirements
Before using GenDTChecker, ensure you have the following:
- **Python 3.6 or higher**: Make sure Python is installed on your system.
- **Dependencies**: Install required packages using pip.
```bash
pip install aiohttp colorama
```

## Installation
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/geniuszlyy/GenDTChecker.git
cd GenDTChecker
```

## Usage
To run GenDTChecker, you can use the following command-line options:
- `-help`: Display help information.
- `-token <your_token>`: Provide the Discord token to check its validity.

## Example
```bash
python GenDTChecker.py -token YOUR_DISCORD_TOKEN
```
Replace `YOUR_DISCORD_TOKEN` with the actual token you want to check.

![image](https://github.com/user-attachments/assets/c4d1bbc2-51c5-47cd-93e6-661dc2a4c1df)


## Output
The tool will display user information in a formatted manner, including the status of the token, user details like username, email, ID, and more. Additionally, it saves this information in a file named `user_data.txt`.

## Disclaimer
This tool is for educational purposes only. Misuse of Discord tokens is against Discord's Terms of Service.


# RU
**GenDTChecker(Gen Discord Token Checker)** - это инструмент на Python, предназначенный для проверки валидности токенов Discord. Он позволяет проверить, активен ли токен, и получить информацию о пользователе, связанного с этим токеном. Инструмент разработан для простоты использования и предоставляет простой интерфейс командной строки с цветным выводом для удобства восприятия.

## Функции
- **Проверка токенов**: Проверка валидности и активности токена Discord.
- **Получение информации о пользователе**: Получение таких данных, как имя пользователя, email, ID, статус телефона и URL аватара.
- **Сохранение данных**: Сохранение полученной информации о пользователе в файл для дальнейшего использования.

## Требования
Перед использованием GenDTChecker убедитесь, что у вас установлены следующие компоненты:
- **Python 3.6 или выше**: Убедитесь, что Python установлен на вашем компьютере.
- **Зависимости**: Установите необходимые пакеты с помощью pip.
```bash
pip install aiohttp colorama
```

## Установка
Клонируйте репозиторий и перейдите в каталог проекта:
```bash
git clone https://github.com/geniuszlyy/GenDTChecker.git
cd GenDTChecker
```

## Использование
Для запуска GenDTChecker используйте следующие параметры командной строки:
- `-help`: Показать справочную информацию.
- `-token <ваш_токен>`: Указать токен Discord для проверки его валидности.

## Пример
```bash
python GenDTChecker.py -token YOUR_DISCORD_TOKEN
```
Замените `YOUR_DISCORD_TOKEN` на фактический токен, который вы хотите проверить.

![image](https://github.com/user-attachments/assets/8f9f843d-cd37-4870-a63f-53762d189f3a)


## Результат
Инструмент отображает информацию о пользователе в формате, включая статус токена, данные пользователя, такие как имя, email, ID и другие. Дополнительно эта информация сохраняется в файл `user_data.txt`.

## Отказ от ответственности
Этот инструмент предназначен только для образовательных целей. Неправомерное использование токенов Discord нарушает Условия использования Discord.
