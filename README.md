Для запуска сборки контейнеров необходмо выполнить скрипт

`./runer`

Будет запущена сборка.
После завершения, перейти по ссылке:

http://127.0.0.1:1337/

Так как проект запущен на gunicorn + nginx, то порт 1337, вместо 8000

Проект построен с использованием стека:
- python 3.10
- django 4
- django rest framework
- jQuery
- Bootstrap 5

Ссылка на документацию API: http://127.0.0.1:1337/docs/

Использование.

Если проект запущен через runer, то будут созданы тестовые данные:
- Пользователь admin, пароль admin
- Пользователь user\_1, пароль user\_1
- Пользователь user\_2, пароль user\_2
- Тестовые табличные данные, 100 записей от начала года, до текущего числа

Если проект предполагается запустить в режиме разработки, необходимо выполнить:

```
cd app
poetry install
poetry run ./manage.py migrate
poetry run ./manage.py makeusers
poetry run ./manage.py adddata
poetry run ./manage.py runserver
```

Будут выполненны следующие действия:

- poetry установит зависимости
- в базе данных будут созданы таблицы
- менедж команад makeusers создаст трёх пользователей
- adddata сгенерирует сто тестовых записей
- runserver запустить приложение

При первом запуске, на странице отобразится пустая таблица данных.

Сначала надо выбрать дату. Может оказаться, что для текущего месяца не сгенериуются данные, т.к. для генерации выбирается случайнфц месяц.

Для добавления новых записей, необходимо войти под пользователем.
После входа появится раздел с полями для добавления записей.

Данная форма добавления поддерживает вставку из таблиц.
