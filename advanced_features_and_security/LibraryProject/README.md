# 📚 LibraryProject

## 🎯 Objective

Gain familiarity with Django by setting up a Django development environment and creating a basic Django project.  
This task introduces you to the workflow of Django projects, including project creation, running the development server, and understanding the default project structure.

---

## ⚙️ Setup Steps

### ✅ 1. Install Django

Make sure Python is installed on your system.  
Then, install Django using pip:

```bash
pip install django
✅ 2. Create a New Django Project
Create a new Django project named LibraryProject:


django-admin startproject LibraryProject
✅ 3. Navigate to the Project Directory

cd LibraryProject
✅ 4. Create README.md
Create this README file inside the LibraryProject directory.
This file serves as documentation for your project setup and structure.

✅ 5. Run the Development Server
Start the Django development server:


python manage.py runserver
Then open your browser and go to:


http://127.0.0.1:8000/
You should see the default Django welcome page, which means your project is working successfully.

🗂️ Project Structure Overview
After running startproject, the following structure will be created:


LibraryProject/
├── LibraryProject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
└── README.md
📄 Key Files and Their Roles
manage.py: Command-line utility to interact with this Django project (runserver, migrations, etc.).

LibraryProject/ (inner folder):

init.py: Marks this directory as a Python package.

settings.py: Contains all project configuration (apps, databases, middleware, etc.).

urls.py: Defines URL routing — acts as the table of contents for your project.

asgi.py / wsgi.py: Entry points for ASGI/WSGI-compatible web servers.

💻 Repository Details
GitHub Repository: Alx_DjangoLearnLab

Directory: Introduction_to_Django

🚀 Next Steps
Create Django apps within the project (e.g., book catalog, user management).

Learn about models, views, templates, and the admin interface.

Implement your own custom features and push updates to your GitHub repository.

Explore deploying your Django project in a production environment.

💬 Contribution
Feel free to fork or clone this repository to kickstart your own Django learning journey!
Pull requests and suggestions are always welcome.

⭐ Happy learning and coding with Django! ⭐
