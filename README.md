# 📝 Django Sticky Notes App

A personal web application built with Django that allows users to register, log in, and manage their own private collection of color-coded sticky notes.

---

## ✨ Features
* 🔐 **User Authentication:** Secure registration, login, and logout functionalities.
* ✍️ **Complete CRUD:** Seamlessly Create, Read, Update, and Delete your notes.
* 🎨 **Custom Colors:** Personalize your dashboard with custom color selection for each sticky note.
* 🛡️ **Privacy:** User-specific private note collections ensuring you only see what belongs to you.

---

## 🚀 Setup Instructions

Follow these steps to get the project up and running on your local machine:

### 1. Install Dependencies
Ensure you have Python installed on your computer. Then, install Django by running the following command in your terminal:
```bash
pip install django
2. Apply Database Migrations
Set up the default SQLite database and create the necessary tables for the application:

Bash
python manage.py migrate
3. Run the Development Server
Start the Django local development server:

Bash
python manage.py runserver
4. Access the Application
Open your favorite web browser and go to the following local address to create an account:
👉 http://127.0.0.1:8000/register/
