Config-Driven Role-Based Access Control (RBAC) System

Project Overview
This project demonstrates a Config-Driven Role-Based Access Control (RBAC) system built using Django.

The system allows an Admin user to dynamically create roles and assign table-level and field-level permissions. Regular users can only access data based on their assigned roles.

Permissions are stored in the database and are NOT hardcoded.

---
Tech Stack
- Backend: Python (Django)
- Database: SQLite
- Frontend: Django Templates (HTML)
- Authentication: Django Built-in Authentication System

---

 Authentication
Admin
- Can create roles
- Can assign permissions
- Has full access to all tables and fields

 Regular Users
- Assigned specific roles
- Can only view/edit based on assigned permissions

---

Sample Tables
- Employees
- Projects
- Roles
- Permissions
- UserRole (Mapping users to roles)

---

 Role & Permission Model

Permissions are configurable at:

 Table Level
- Can View Table
- Can Edit Table

 Field Level
- Can View Specific Column
- Can Edit Specific Column

Example:
- Viewer → Can view employee table but salary column hidden
- Editor → Can view and edit employee table
- Manager → Full access

---

 Access Enforcement
- Tables without permission are hidden
- Fields without view permission are hidden
- Edit is blocked if permission not granted
- Unauthorized actions are rejected by backend

---

 How to Run the Project

1. Clone the repository
2. Install dependencies:
   pip install django
3. Run migrations:
   python manage.py migrate
4. Create superuser:
   python manage.py createsuperuser
5. Run server:
   python manage.py runserver
6. Open:
   http://127.0.0.1:8000/

---

 Sample Login Credentials

Admin:
Username: admin
Password: admin123

Regular User:
Username: user1
Password: jasber123

---

Core Features
- Config-driven permission system
- Dynamic role creation
- Table-level access control
- Field-level access control
- Backend permission validation
- Role-based UI behavior

---

 Conclusion
This project demonstrates a secure and dynamic RBAC system where permissions are fully configurable by an Admin and enforced strictly at the backend.
