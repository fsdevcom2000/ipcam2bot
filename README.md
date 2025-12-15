# IP Camera Monitoring Bot / Бот для мониторинга IP-камер

## English

### Description
This Telegram bot monitors multiple IP cameras using YOLOv8 for human detection. When a person is detected on a camera, the bot sends a photo to the associated Telegram user. The bot is asynchronous and built with **Aiogram 3**, **OpenCV**, and **SQLite3**.

### Features
- Add, remove, and list cameras for each user
- Human detection on camera snapshots using YOLOv8
- Sends alert photos via Telegram
- Cooldown system to avoid sending duplicate alerts too frequently
- Stores cameras in an SQLite3 database

### Installation
1. Clone the repository:
2. Install dependencies:

`pip install -r requirements.txt`

3. Configure `settings/config.py` with your bot token and admin chat ID.
### Usage

Run the bot:

`python3 main.py`

The bot will start polling and monitoring cameras automatically.

### Database

SQLite3 database (`cameras.db`) stores cameras with the following fields:

- `id` — Camera ID
- `user_id` — Telegram user ID
- `name` — Camera name
- `url` — RTSP/HTTP camera URL
---

## Русский

### Описание

Этот Telegram-бот мониторит несколько IP-камер с использованием YOLOv8 для обнаружения людей. Когда человек обнаружен на камере, бот отправляет фото пользователю Telegram. Бот асинхронный, использует **Aiogram 3**, **OpenCV** и **SQLite3** для хранения камер.

### Возможности

- Добавление, удаление и просмотр списка камер для каждого пользователя
- Обнаружение людей на кадрах камер с помощью YOLOv8
- Отправка фото-уведомлений через Telegram
- Система cooldown для предотвращения частых повторных уведомлений
- Хранение камер в базе данных SQLite3

### Установка

1. Клонировать репозиторий:
2. Установить зависимости:
3. 
`pip install -r requirements.txt`

4. Настроить файл `settings/config.py` с токеном бота и ID чата администратора.

### Запуск

Запустить бота:

`python3 main.py`

Бот автоматически начнёт polling и мониторинг камер.

### База данных

SQLite3 база (`cameras.db`) хранит камеры с полями:

- `id` — ID камеры
- `user_id` — Telegram ID пользователя
- `name` — Название камеры
- `url` — RTSP/HTTP URL камеры
