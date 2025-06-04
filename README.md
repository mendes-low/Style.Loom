# StyleLoom

**StyleLoom** is an online fashion store where you can find the latest trends as well as classic clothing for men, women, and children.

## 🚀 Features
- Browse product catalog
- Filter products by categories (Men's, Women's, Kids)
- Product detail page

## 🛠️ Technologies
- **Backend:** Django  
- **Frontend:** HTML, CSS  
- **Database:** SQLite (default)  
- **Templates:** Django Template Language (DTL)

---

## 📦 Installation & Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/mendes-low/Style.Loom
cd styleLoom
```

### 2️⃣ Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate  # For MacOS/Linux
venv\Scripts\activate     # For Windows
```

### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Apply migrations
```
python manage.py migrate
```

### 5️⃣ Create a superuser (optional)
```
python manage.py createsuperuser
```
#### Enter a username, email, and password for admin access.

### 6️⃣ Run the server
```
python manage.py runserver
```
