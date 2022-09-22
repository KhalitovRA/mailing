# mailing
1. Клонируйте репозиторий с github. (git clone https://github.com/KhalitovRA/mailing)
2. Создайте виртуальное окружение (python -m venv venv).
3. Установите зависимости 'pip install -r requirements.txt' 
4. Впишите константы в файл .env 
5. Запускайте сервер ('python manage.py runserver')

-------------------------------------------------------------------------------------

http://127.0.0.1:8000/api/client/ - Создание клиента
http://127.0.0.1:8000/api/client/{id}/ - Изменение параметров клиента
http://127.0.0.1:8000/api/clientdelete/{id}/ - Удаление клиента из справочника
http://127.0.0.1:8000/api/messages/ - Список сообщений
http://127.0.0.1:8000/api/mailing/ - Создание рассылки
http://127.0.0.1:8000/api/mailing/{id}/ - Изменение рассылки
http://127.0.0.1:8000/api/mailingdelete/{id}/ - Удаление рассылки
http://127.0.0.1:8000/swagger/ - OpenAPI документация