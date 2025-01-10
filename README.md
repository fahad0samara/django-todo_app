# Time Management Todo App 📝

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Django](https://img.shields.io/badge/Django-4.x-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A comprehensive task management application built with Django that helps you organize, prioritize, and track your daily tasks efficiently. This application is designed to boost your productivity and help you maintain a better work-life balance. ⚡

## ✨ Features

### 📋 Task Management
- ✅ Create, read, update, and delete tasks
- ⏰ Set due dates and reminders
- ✓ Mark tasks as complete/incomplete
- 📝 Add detailed descriptions to tasks
- 🎯 Categorize tasks by priority (High, Medium, Low)
- 🏷️ Add labels/tags for better organization

### 🎨 User Interface
- 💻 Clean and intuitive dashboard
- 📱 Responsive design that works on desktop and mobile
- 🌓 Dark/Light mode support
- 🔄 Easy drag-and-drop task reordering
- 🔍 Filter tasks by status, priority, or date
- 🔎 Search functionality to quickly find tasks

### 📊 Task Organization
- 📈 Sort tasks by priority, due date, or creation date
- 📂 Group tasks by categories
- 📦 Archive completed tasks
- ⚡ Bulk actions for multiple tasks
- 📊 Progress tracking and statistics

## 🛠️ Technologies Used

### Backend
- 🐍 Python 3.x
- 🎯 Django 4.x
- 💾 SQLite3 database
- 🔌 Django REST framework for API

### Frontend
- 📄 HTML5
- 🎨 CSS3
- ⚡ JavaScript
- 🎯 Bootstrap for responsive design

## 🚀 Quick Start

### Prerequisites
- Python 3.x
- pip (Python package manager)
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/fahad0samara/django-Todo-App.git
cd django-Todo-App
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
```

3. Install dependencies:
```bash
pip install django
```

4. Setup database:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create admin account:
```bash
python manage.py createsuperuser
```

6. Run the server:
```bash
python manage.py runserver
```

7. Open your browser:
   - Main app: `http://localhost:8000`
   - Admin panel: `http://localhost:8000/admin`

## 📱 App Screenshots

[Add your app screenshots here]

## 💡 Usage Guide

### 📝 Creating Tasks
1. Click the "Add Task" button
2. Fill in task details:
   - 📌 Title (required)
   - 📄 Description (optional)
   - 📅 Due date
   - 🎯 Priority level
   - 🏷️ Labels/tags
3. Click "Save"

### ⚡ Managing Tasks
- 👆 Click task to view/edit details
- ✅ Use checkbox to mark complete
- 🎯 Click priority to change level
- 🔍 Use filters in sidebar
- 🔎 Search for specific tasks

### 📂 Task Categories
- 👤 Personal
- 💼 Work
- 🛒 Shopping
- 💪 Health
- 📚 Education
- 📌 Others

## 📁 Project Structure

```
todo_app/
├── 📁 tasks/                # Main application directory
│   ├── 📁 migrations/      # Database migrations
│   ├── 📁 static/         # Static files
│   │   ├── 📁 css/       # Stylesheets
│   │   ├── 📁 js/        # JavaScript
│   │   └── 📁 images/    # Images
│   ├── 📁 templates/      # HTML templates
│   │   ├── 📄 base.html  # Base template
│   │   └── 📁 tasks/     # Task templates
│   ├── 📄 admin.py       # Admin config
│   ├── 📄 models.py      # Database models
│   ├── 📄 urls.py        # URL config
│   └── 📄 views.py       # View functions
├── 📁 todo_app/           # Project settings
├── 📄 manage.py          # Django CLI
└── 📄 db.sqlite3         # Database
```

## 🧪 Development

### Running Tests
```bash
python manage.py test
```

### 📝 Code Style
We follow PEP 8 style guide for Python code. Please ensure your contributions maintain these standards.

## 🤝 Contributing

1. 🔱 Fork the repository
2. 🌿 Create feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit changes (`git commit -m 'Add AmazingFeature'`)
4. 📤 Push to branch (`git push origin feature/AmazingFeature`)
5. 📬 Open a Pull Request

## 💬 Support

Need help? Here's what to do:
1. 📚 Check documentation
2. 🔍 Search existing issues
3. ❓ Create new issue if needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- 🎯 Django documentation and community
- 🎨 Bootstrap for the responsive design
- 👥 All contributors

---
Made with ❤️ by [Fahad]
