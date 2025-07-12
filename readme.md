# Employ Morning Exercise App

## Overview

This Django web application efficiently manages employee attendance for morning exercises. It offers a simple card scanning interface, displays real-time attendance information, and includes a robust administrative panel for data management and reporting.

---

## Features

* **Employee Card Scanning:** Quick attendance recording by entering unique employee IDs.
* **Real-time Information:** Instantly displays the scanned employee's name, department, last scan time, and status on the main page.
* **Recent Scans Log:** Shows the last 50 attendance records in a clear table format on the main interface.
* **Django Admin Panel:**
    * **Employee Management:** Full CRUD (Create, Read, Update, Delete) operations for employee profiles.
    * **Attendance Tracking:** View, filter, and manually add scan records with statuses like 'Present', 'Late', or 'Absent'.
    * **Date-based Reporting:** Easily filter and export attendance data by specific dates using the integrated `django-import-export` tool.
* **Attractive & Responsive UI:** Built with **Tailwind CSS** for a modern, clean, and mobile-friendly design.
* **Offline Functionality:** Tailwind CSS is added locally, ensuring the application's styling works flawlessly without an internet connection.
* **Thailand Time Zone Support:** Attendance status (e.g., 'Late' after 9:00 AM) is determined using the 'Asia/Bangkok' timezone.

---

## Technologies Used

* **Django:** High-level Python web framework.
* **SQLite:** Lightweight, file-based database (default for development).
* **Python 3.x**
* **`django-import-export`:** Facilitates data import and export within the Django admin.



## Project Structure

```text
EmployMorningExerciseApp/
|
├── morning_exercise/ 
|   ├── asgi.py             
│   ├── settings.py         # Contain Timezone
│   ├── urls.py      
│   └── wsgi.py             
├── scanner/                
│   ├── migrations/         # Database schema changes
│   ├── static/             # Static files 
│   │   └── style.css
│   ├── templates/          # HTML templates 
│   │   └── index.html
│   │       
│   ├── admin.py            # Admin panel customizations
│   ├── app.py            
│   ├── models.py           # Database models (Employee, ScanRecord)
│   ├── tests.py            
│   ├── urls.py             
│   └── views.py            # Application logic (handling requests, data processing)
├── db.sqlite3              # SQLite database file
├── manage.py               # Django's command-line utility
├── requirements.txt        # Python dependencies list
└── README.md               # Project overview and documentation
```





## Project Setup and Run

Follow these steps to get the application running on your local machine.

### 1. Prerequisites

Make sure you have the following installed:

* **Python 3.x**: Download from [python.org](https://www.python.org/downloads/).

### 2. Clone the Repository

Start by cloning this Git repository:

```bash
git clone [https://github.com/abyshergill/EmployMorningExerciseApp.git]
cd EmployMorningExerciseApp      
```

### 3. Inside folder EmployMorningExerciseApp / 

* **Create Virtual Enviroment** 
```bash
## For windows
python -m venv .env            ## Note .env you can use any name as you want
```
* **Activate the virtual Enviroment**
```bash
## For windows
.env\scripts\activate          ## After activate .env will appear in cmd path
```

* **Install the necessary dependcies**

```bash
## For windows
pip install -r requirements.txt          
```

* **Run the Main Program**

```bash
## For windows
python manage.py runserver          
```

* **Access the Admin Panel**

```bash
## Inside your Browswer
http://127.0.0.1:8000/admin         

username : admin
password : admin

Testing Employ
user1
user2
user3
user4
user5
```