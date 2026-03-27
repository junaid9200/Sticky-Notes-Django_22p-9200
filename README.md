# Django Sticky Notes App

A personal web application built with Django that allows users to register, log in, and manage their own private collection of color-coded sticky notes.

## Features
- User Authentication (Registration, Login, Logout)
- Create, Read, Update, and Delete (CRUD) notes
- Custom color selection for each sticky note
- User-specific private note collections

## Setup Instructions

Follow these steps to run the project on your local machine:

### 1. Install Dependencies
Make sure you have Python installed, then install Django by running:
pip install django
Set up the SQLite database and create the necessary tables:
python manage.py migrate
Start the Django server:
python manage.py runserver
Open your web browser and go to:
https://www.google.com/search?q=http://127.0.0.1:8000/register/
