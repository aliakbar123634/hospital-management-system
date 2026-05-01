# 🏥 Hospital Management System (Django + DRF)

## 📌 Overview

This project is a **Hospital Management System API** built using **Django** and **Django REST Framework (DRF)**.

It handles core hospital workflows including:

* Patient management
* Doctor scheduling
* Appointment booking
* Prescription handling
* Billing & invoices

⚠️ Note:
This project currently includes **backend APIs only**.
Frontend (UI) is **not implemented yet**.

---

## 🚀 Tech Stack

* Python
* Django
* Django REST Framework (DRF)
* SQLite / PostgreSQL (configurable)
* JWT / Token Authentication (if implemented)

---

## 📂 Project Structure

```
project/
│
├── accounts/        # User & role management
├── patients/        # Patient profiles & medical history
├── doctors/         # Doctor profiles & schedules
├── appointments/    # Appointment booking system
├── prescriptions/   # Prescriptions & lab reports
├── billing/         # Invoices & payments
├── core/            # Shared utilities (optional)
│
├── manage.py
└── requirements.txt
```

---

## ⚙️ Features

### 👤 Accounts

* Custom user model
* Role-based system:

  * Admin
  * Doctor
  * Patient
  * Receptionist

---

### 🧑‍⚕️ Patients

* Patient profile management
* Medical history tracking

---

### 👨‍⚕️ Doctors

* Doctor profile
* Availability & scheduling

---

### 📅 Appointments

* Book appointments
* Manage appointment status
* Link patients with doctors

---

### 💊 Prescriptions

* Create prescriptions
* Attach to appointments
* Upload lab reports

---

### 💰 Billing

* Generate invoices
* Payment tracking
* (Optional) PDF invoice generation

---

## 🔌 API Endpoints (Sample)

```
/api/accounts/
/api/patients/
/api/doctors/
/api/appointments/
/api/prescriptions/
/api/billing/
```

Each module uses DRF ViewSets:

* List
* Create
* Retrieve
* Update
* Delete

---

## 🔐 Authentication

* Token-based / JWT authentication (depending on implementation)

---

## 🧠 Architecture

* DRF handles all business logic and API responses
* Modular app structure for scalability
* Role-based access control (planned / partial)

---

## ❌ Current Limitations

* No frontend (Django templates / React not implemented)
* Notifications (SMS/Email) not added yet
* Advanced permissions may be incomplete
* Payment gateway not integrated

---

## 🛠️ Setup Instructions

### 1. Clone repository

```
git clone <repo-url>
cd project
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Run server

```
python manage.py runserver
```

---

## 📌 Future Improvements

* Add frontend (React / Django Templates)
* Implement notifications (SMS/Email)
* Add advanced role-based permissions
* Integrate payment gateway
* Improve API validation & security

---

## 👨‍💻 Author

Ali Akbar Shah

---

## ⚠️ Disclaimer

This is a **learning/project-level implementation**, not production-ready yet.
