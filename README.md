# 🛠️ Django IT Support & Helpdesk System

**Django IT Support** — бұл IT-қолдау қызметіне келіп түсетін өтінімдерді (тикеттерді) тіркеу, бақылау және басқаруға арналған веб-қосымша.

## 🚀 Негізгі мүмкіндіктер
- 📝 Жаңа IT-өтінімдер (тикеттер) құру және жіберу
- 📊 Өтінімдердің мәртебесін бақылау (Жаңа, Орындалуда, Жабық)
- 🔐 Қолданушылар мен әкімшілерге арналған рөлдер жүйесі
- ⚡ Жылдам әрі ыңғайлы веб-интерфейс

## 🛠️ Қолданылған технологиялар
- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3
- **Database:** SQLite / PostgreSQL

## 💻 Локалды түрде іске қосу (Installation)

1. Репозиторийді көшіріп алыңыз:
   ```bash
   git clone https://github.com
   cd django-it-support
   ```
2. Виртуалды орта құрып, іске қосыңыз:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Қажетті кітапханаларды орнатыңыз:
   ```bash
   pip install -r requirements.txt
   ```
4. Миграцияларды орындап, серверді қосыңыз:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
