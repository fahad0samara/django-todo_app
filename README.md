# Time Management Todo App

A comprehensive task management application built with Django that helps you organize, prioritize, and track your daily tasks efficiently. This application is designed to boost your productivity and help you maintain a better work-life balance.

## Features

- **Task Management**
  - Create, read, update, and delete tasks
  - Set due dates and reminders
  - Mark tasks as complete/incomplete
  - Add detailed descriptions to tasks
  - Categorize tasks by priority (High, Medium, Low)
  - Add labels/tags to tasks for better organization

- **User Interface**
  - Clean and intuitive dashboard
  - Responsive design that works on desktop and mobile
  - Dark/Light mode support
  - Easy drag-and-drop task reordering
  - Filter tasks by status, priority, or date
  - Search functionality to quickly find tasks

- **Task Organization**
  - Sort tasks by priority, due date, or creation date
  - Group tasks by categories
  - Archive completed tasks
  - Bulk actions for multiple tasks
  - Progress tracking and statistics

## Technologies Used

- **Backend**
  - Python 3.x
  - Django 4.x
  - SQLite3 database
  - Django REST framework for API

- **Frontend**
  - HTML5
  - CSS3
  - JavaScript
  - Bootstrap for responsive design

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
```

3. Install the required dependencies:
```bash
pip install django
```

4. Run database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

7. Visit `http://localhost:8000` in your web browser to use the application.
   Admin panel is available at `http://localhost:8000/admin`

## Usage Guide

### Creating Tasks
1. Click on the "Add Task" button
2. Fill in the task details:
   - Title (required)
   - Description (optional)
   - Due date
   - Priority level
   - Labels/tags
3. Click "Save" to create the task

### Managing Tasks
- Click on a task to view/edit its details
- Use the checkbox to mark tasks as complete
- Click the priority indicator to change task priority
- Use filters in the sidebar to sort and organize tasks
- Use the search bar to find specific tasks

### Task Categories
- Personal
- Work
- Shopping
- Health
- Education
- Others

## Project Structure

```
todo_app/
├── tasks/                  # Main application directory
│   ├── migrations/        # Database migrations
│   ├── static/           # Static files (CSS, JS)
│   │   ├── css/         # Stylesheet files
│   │   ├── js/          # JavaScript files
│   │   └── images/      # Image assets
│   ├── templates/        # HTML templates
│   │   ├── base.html    # Base template
│   │   └── tasks/       # Task-specific templates
│   ├── admin.py         # Admin configuration
│   ├── models.py        # Database models
│   ├── urls.py          # URL configurations
│   └── views.py         # View functions
├── todo_app/             # Project settings directory
├── manage.py            # Django management script
└── db.sqlite3           # SQLite database
```

## Development

### Running Tests
```bash
python manage.py test
```

### Code Style
This project follows PEP 8 style guide for Python code. Please ensure your contributions adhere to these standards.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Support

If you encounter any issues or have questions, please:
1. Check the documentation
2. Look through existing issues
3. Create a new issue if needed

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Django documentation and community
- Bootstrap for the responsive design
- All contributors who help improve this project
