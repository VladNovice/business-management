```
Файл/Папка	Назначение
main.py	Точка входа в приложение FastAPI. Здесь создается экземпляр FastAPI и подключаются роутеры.
business_monitor.db	SQLite-база данных для хранения информации (пользователи, проекты и т.д.).
tests/	Папка для модульных и интеграционных тестов (пока пустая).
venv/	Виртуальное окружение Python с установленными зависимостями.
Backend (FastAPI)
app/backend/
Путь	Назначение
api/routers/	Роутеры для обработки HTTP-запросов.
→ users.py	Эндпоинты для работы с пользователями (регистрация, аутентификация).
→ projects.py	API для управления проектами (создание, обновление, удаление).
→ deps.py	Зависимости (Depends) для роутеров (например, get_current_user).
core/	Базовые настройки и утилиты.
→ config.py	Конфигурация приложения (настройки из переменных окружения).
→ security.py	Логика аутентификации (JWT-токены, хеширование паролей).
database/	Работа с базой данных.
→ base.py	Подключение к БД (например, Base = declarative_base()).
→ models.py	SQLAlchemy-модели таблиц (User, Project).
→ __init__.py	Инициализация пакета (может содержать фабрику сессий БД).
schemas/	Pydantic-схемы для валидации данных.
→ user.py	Схемы для входных/выходных данных пользователя (UserCreate, UserResponse).
→ project.py	Схемы для проектов (ProjectCreate, ProjectUpdate).
Frontend (HTML/CSS/JS)
app/frontend/
Путь	Назначение
static/	Статические файлы (CSS, JS, изображения).
→ static.css	Глобальные стили для всех страниц.
→ static.js	Клиентские скрипты (AJAX-запросы к API, обработка событий).
templates/	HTML-шаблоны для рендеринга страниц.
→ base.html	Базовый шаблон с общим布局 (header, footer, подключение CSS/JS).
Служебные файлы
Путь	Назначение
__pycache__/	Кэш-файлы Python (автогенерируются, не редактируются).
venv/	Виртуальное окружение (установленные пакеты fastapi, sqlalchemy и т.д.).
```

















```
business-management
├─ app
│  ├─ backend
│  │  ├─ api
│  │  │  └─ routers
│  │  │     ├─ deps.py
│  │  │     ├─ projects.py
│  │  │     ├─ users.py
│  │  │     └─ __pycache__
│  │  │        └─ users.cpython-313.pyc
│  │  ├─ core
│  │  │  ├─ config.py
│  │  │  ├─ security.py
│  │  │  └─ __pycache__
│  │  │     ├─ config.cpython-313.pyc
│  │  │     └─ security.cpython-313.pyc
│  │  ├─ database
│  │  │  ├─ base.py
│  │  │  ├─ models.py
│  │  │  ├─ __init__.py
│  │  │  └─ __pycache__
│  │  │     ├─ base.cpython-313.pyc
│  │  │     ├─ models.cpython-313.pyc
│  │  │     └─ __init__.cpython-313.pyc
│  │  └─ schemas
│  │     ├─ project.py
│  │     ├─ user.py
│  │     └─ __pycache__
│  │        └─ user.cpython-313.pyc
│  └─ frontend
│     ├─ static
│     │  ├─ static.css
│     │  └─ static.js
│     └─ templates
│        └─ base.html
├─ business_monitor.db
├─ main.py
├─ tests
├─ venv
```