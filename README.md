# Board Games API

Это учебный проект на Django REST framework.

Тема проекта: клуб настольных игр. В API есть категории игр, настольные игры и отзывы.

## Как запустить

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

API:
http://127.0.0.1:8000/api/v1/

Swagger:
http://127.0.0.1:8000/api/schema/swagger-ui/

Админка:
http://127.0.0.1:8000/admin/

Логин и пароль для админки:
admin
admin12345

## Модели

Category - категория настольной игры.
Поля: id, name, description.

BoardGame - настольная игра.
Поля: id, title, category, category_id, min_players, max_players, play_time, difficulty, is_available, description, created_at.

Review - отзыв на игру.
Поля: id, game, game_id, author_name, rating, text, created_at.

## Эндпоинты

Категории:
GET    /api/v1/categories/
GET    /api/v1/categories/{id}/
POST   /api/v1/categories/
PATCH  /api/v1/categories/{id}/
DELETE /api/v1/categories/{id}/

Игры:
GET    /api/v1/games/
GET    /api/v1/games/{id}/
POST   /api/v1/games/
PATCH  /api/v1/games/{id}/
DELETE /api/v1/games/{id}/

Фильтры для игр:
GET /api/v1/games/?category=1
GET /api/v1/games/?min_players=2
GET /api/v1/games/?max_players=4
GET /api/v1/games/?is_available=true

Групповые запросы для игр:
POST   /api/v1/games/bulk_create/
PATCH  /api/v1/games/bulk_update/
DELETE /api/v1/games/bulk_delete/

Пример для bulk_create:
[
  {
    "title": "Catan",
    "category_id": 1,
    "min_players": 3,
    "max_players": 4,
    "play_time": 90,
    "difficulty": "medium",
    "is_available": true,
    "description": "Board game"
  }
]

Пример для bulk_delete:
{
  "ids": [1, 2, 3]
}

Отзывы:
GET    /api/v1/reviews/
GET    /api/v1/reviews/{id}/
POST   /api/v1/reviews/
PATCH  /api/v1/reviews/{id}/
DELETE /api/v1/reviews/{id}/

Фильтр отзывов:
GET /api/v1/reviews/?game_id=1

## Библиотеки

Все библиотеки записаны в requirements.txt.
