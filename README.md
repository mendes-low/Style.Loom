# StyleLoom

StyleLoom – это интернет-магазин модной одежды, где можно найти как последние тренды, так и классическую одежду для мужчин, женщин и детей.

## 🚀 Функционал
- Просмотр каталога товаров
- Фильтрация товаров по категориям (Men's, Women's, Kids)
- Страница с деталями товара

## 🛠️ Технологии
- **Backend:** Django
- **Frontend:** HTML, CSS
- **База данных:** SQLite (по умолчанию)
- **Шаблоны:** Django Template Language (DTL)

---

## 📦 Установка и запуск

### 1️⃣ Клонирование репозитория
```
git clone https://github.com/mendes-low/Style.Loom
cd styleLoom
```

### 2️⃣ Создание и активация виртуального окружения 
```
python -m venv venv
source venv/bin/activate  # Для MacOS/Linux
venv\Scripts\activate     # Для Windows
```

### 3️⃣ Установка зависимостей
```
pip install -r requirements.txt
```

### 4️⃣ Применение миграций
```
python manage.py migrate
```

### 5️⃣ Создание суперпользователя (необязательно)
```
python manage.py createsuperuser
```
#### Введи имя, email и пароль для входа в админку.

### 6️⃣ Запуск сервера
```
python manage.py runserver
```