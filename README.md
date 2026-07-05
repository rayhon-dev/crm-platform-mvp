<div align="center">

# 🎓 EduCRM

<p align="center">
  <b>Choose a language to view the project description:</b>
</p>

[![English](https://img.shields.io/badge/GB-English-blue?style=for-the-badge)](README.md#english)
[![Russian](https://img.shields.io/badge/RU-Русский-blue?style=for-the-badge)](README.md#russian)
[![Uzbek](https://img.shields.io/badge/UZ-O'zbekcha-blue?style=for-the-badge)](README.md#uzbek)

</div>

---

## English

<div id="english">

### 🎓 EduCRM — Learning Center Management System

A comprehensive CRM system for educational centers built with Django REST Framework.

#### 🚀 Features

- **Authentication** — JWT-based auth with role-based access control
- **Students** — Full CRUD with profile management
- **Teachers** — Full CRUD with subject and salary tracking
- **Courses** — Course management with pricing
- **Groups** — Group management with schedule and student enrollment
- **Attendance** — Bulk attendance tracking with statistics
- **Assignments** — Assignment creation, submission, and grading system
- **Payments** — Manual payment tracking with debt monitoring
- **Notifications** — User notification system
- **Dashboard** — Admin statistics overview

#### 🛠 Tech Stack

| Technology | Version |
|---|---|
| Python | 3.12 |
| Django | 6.0 |
| Django REST Framework | 3.x |
| PostgreSQL | 17 |
| JWT | djangorestframework-simplejwt |
| Docker | latest |

#### 📦 Installation

**1. Clone the repository**
```bash
git clone https://github.com/rayhon-dev/crm-platform-mvp.git
cd crm-platform-mvp
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Setup environment variables**
```bash
cp .env.example .env
# Edit .env with your database credentials
```

**5. Run migrations**
```bash
python manage.py migrate
```

**6. Seed database**
```bash
python manage.py seed
```

**7. Run server**
```bash
python manage.py runserver
```

#### 🐳 Docker

```bash
docker-compose up --build
```

#### 📚 API Documentation

After running the server, visit: http://127.0.0.1:8000/api/docs/

#### 👤 Default Users (after seed)

| Role | Username | Password |
|---|---|---|
| Admin | admin | admin12345 |
| Teacher | teacher_sardor | test12345 |
| Student | student_ali | test12345 |

#### 🔑 API Endpoints

| Module | Endpoint | Methods |
|---|---|---|
| Auth | `/api/auth/login/` | POST |
| Auth | `/api/auth/refresh/` | POST |
| Auth | `/api/auth/me/` | GET |
| Students | `/api/students/` | GET, POST |
| Teachers | `/api/teachers/` | GET, POST |
| Courses | `/api/courses/` | GET, POST |
| Groups | `/api/groups/` | GET, POST |
| Attendance | `/api/attendance/` | GET, POST |
| Assignments | `/api/assignments/` | GET, POST |
| Payments | `/api/payments/` | GET, POST |
| Notifications | `/api/notifications/` | GET, POST |
| Dashboard | `/api/dashboard/` | GET |

</div>

---

## Русский

<div id="russian">

### 🎓 EduCRM — Система управления учебным центром

Комплексная CRM-система для учебных центров, разработанная на Django REST Framework.

#### 🚀 Возможности

- **Аутентификация** — JWT-авторизация с ролевым доступом
- **Студенты** — Полный CRUD с управлением профилями
- **Преподаватели** — Полный CRUD с отслеживанием предмета и зарплаты
- **Курсы** — Управление курсами с ценообразованием
- **Группы** — Управление группами с расписанием и записью студентов
- **Посещаемость** — Массовое отслеживание посещаемости со статистикой
- **Задания** — Создание, сдача и оценка заданий
- **Платежи** — Ручное отслеживание платежей с мониторингом долгов
- **Уведомления** — Система уведомлений пользователей
- **Дашборд** — Обзор статистики для администратора

#### 📦 Установка

**1. Клонировать репозиторий**
```bash
git clone https://github.com/rayhon-dev/crm-platform-mvp.git
cd crm-platform-mvp
```

**2. Создать виртуальное окружение**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

**3. Установить зависимости**
```bash
pip install -r requirements.txt
```

**4. Настроить переменные окружения**
```bash
cp .env.example .env
# Заполните .env данными вашей базы данных
```

**5. Выполнить миграции**
```bash
python manage.py migrate
```

**6. Заполнить базу данных тестовыми данными**
```bash
python manage.py seed
```

**7. Запустить сервер**
```bash
python manage.py runserver
```

#### 🐳 Docker

```bash
docker-compose up --build
```

#### 📚 Документация API

После запуска сервера перейдите по адресу: http://127.0.0.1:8000/api/docs/

#### 👤 Пользователи по умолчанию (после seed)

| Роль | Логин | Пароль |
|---|---|---|
| Администратор | admin | admin12345 |
| Преподаватель | teacher_sardor | test12345 |
| Студент | student_ali | test12345 |

</div>

---

## O'zbekcha

<div id="uzbek">

### 🎓 EduCRM — O'quv Markaz Boshqaruv Tizimi

Django REST Framework asosida qurilgan o'quv markazlari uchun kompleks CRM tizimi.

#### 🚀 Imkoniyatlar

- **Autentifikatsiya** — Rol asosida JWT autentifikatsiya
- **O'quvchilar** — To'liq CRUD va profil boshqaruvi
- **O'qituvchilar** — To'liq CRUD, fan va maosh kuzatuvi
- **Kurslar** — Narx bilan kurs boshqaruvi
- **Guruhlar** — Jadval va o'quvchi biriktirish bilan guruh boshqaruvi
- **Davomat** — Statistika bilan ommaviy davomat kuzatuvi
- **Topshiriqlar** — Topshiriq yaratish, yuborish va baholash tizimi
- **To'lovlar** — Qarzdorlik monitoringi bilan qo'lda to'lov kuzatuvi
- **Bildirishnomalar** — Foydalanuvchi bildirishnoma tizimi
- **Dashboard** — Admin statistika paneli

#### 📦 O'rnatish

**1. Repozitoriyani klonlash**
```bash
git clone https://github.com/rayhon-dev/crm-platform-mvp.git
cd crm-platform-mvp
```

**2. Virtual muhit yaratish**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

**3. Paketlarni o'rnatish**
```bash
pip install -r requirements.txt
```

**4. Muhit o'zgaruvchilarini sozlash**
```bash
cp .env.example .env
# .env faylini ma'lumotlar bazasi ma'lumotlari bilan to'ldiring
```

**5. Migratsiyalarni bajarish**
```bash
python manage.py migrate
```

**6. Test ma'lumotlarni yuklash**
```bash
python manage.py seed
```

**7. Serverni ishga tushirish**
```bash
python manage.py runserver
```

#### 🐳 Docker

```bash
docker-compose up --build
```

#### 📚 API Hujjatlari

Serverni ishga tushirgandan so'ng: http://127.0.0.1:8000/api/docs/

#### 👤 Standart foydalanuvchilar (seed dan keyin)

| Rol | Username | Parol |
|---|---|---|
| Admin | admin | admin12345 |
| O'qituvchi | teacher_sardor | test12345 |
| O'quvchi | student_ali | test12345 |

</div>

---

<div align="center">

Made by [Rayhon](https://github.com/rayhon-dev)

</div>