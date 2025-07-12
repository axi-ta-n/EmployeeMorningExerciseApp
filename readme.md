# 🏋️‍♂️ Employ Morning Exercise App

A modern Django web application to efficiently manage employee attendance for morning exercises via a card-scanning system. Built with simplicity, speed, and style in mind.

---

## 📌 Overview

This Django-based system allows:
- 🪪 Quick ID-based attendance via card scanning
- 🧑‍💼 Real-time display of employee info
- 📋 Instant logging of attendance records
- 🛠️ Admin control panel for full data management
- 🌐 Offline-ready responsive UI
- 🕘 Smart time-based attendance marking using Bangkok timezone

---

## ✨ Features

- 🔐 **Employee Card Scanning**  
  → Fast, ID-based attendance logging on the main interface.

- ⏱ **Real-Time Info Display**  
  → Instantly shows employee's name, department, last scan, and status.

- 📊 **Recent Scans Log**  
  → View the last 50 scan records clearly in a live-updating table.

- ⚙️ **Django Admin Panel**
  - 👤 Employee CRUD operations
  - 📅 Attendance view & manual record support (Present, Late, Absent)
  - 🧾 Date-wise filtering & export (via `django-import-export`)

- 💅 **Responsive UI with Tailwind CSS**  
  → Clean, mobile-friendly interface with offline Tailwind integration.

- 🕰️ **Timezone Support**  
  → Attendance marked based on Bangkok Time (`Asia/Bangkok`); e.g., 'Late' after 9:00 AM.

---

## 🛠️ Technologies Used

| Tool               | Purpose                                |
|--------------------|----------------------------------------|
| 🐍 Python 3.x       | Core programming language              |
| 🌐 Django          | Web framework                          |
| 🗃️ SQLite           | Lightweight development DB             |
| 🛍️ Tailwind CSS     | UI styling                             |
| 📥 django-import-export | Easy data export/import via admin panel |

---

## 🗂️ Project Structure

```text
EmployMorningExerciseApp/
│
├── morning_exercise/ 
│   ├── settings.py         # Contains timezone settings
│   └── urls.py             # URL routing
│
├── scanner/
│   ├── static/             # Local Tailwind CSS
│   ├── templates/          # index.html interface
│   ├── models.py           # Employee & ScanRecord models
│   ├── admin.py            # Admin customizations
│   └── views.py            # Request handling & logic
│
├── db.sqlite3              # SQLite database
├── manage.py               # Django utility script
├── requirements.txt        # Dependency list
└── README.md               # You are here 🚀
