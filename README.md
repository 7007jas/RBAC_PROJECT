Config-Driven RBAC System (Django)

About This Project:
   
- I built this project to understand how real-world applications handle role-based access control (RBAC).
- I designed the system in a way where the Admin can dynamically create roles and assign permissions from the database itself.

The main idea of this project is:

- Access control should be configurable, not hardcoded. This system supports both table-level and field-level permissions.

Tech Used:

1) Python (Django)
2) SQLite (default Django DB)
3) Django Templates (HTML)
4) Django Authentication System
- I chose Django because it provides built-in authentication and makes permission handling easier to implement cleanly.

How the System Works

There are two main types of users:

1. Admin:

- Can create roles
- Can assign permissions to roles
- Has full access to all tables and fields
- Controls what other users can see or edit

2. Regular Users:

- Assigned a specific role
- Can only access tables and fields based on their role permissions
- Cannot perform any action outside their permission scope
  
Database Structure:

The main tables used in this project:

- Employees, Projects, Roles, Permissions, UserRole
- Permissions are stored in the database and linked to roles.
  
Permission Types:

Permissions are handled at two levels:

1) Table Level:

- Can view a table
- Can edit a table

2) Field Level:

- Can view specific columns
- Can edit specific columns

Access Control Logic:

- If a user does not have permission to view a table, the table is not shown.
- If a user does not have permission to view a field, that field is hidden.
- If edit permission is not granted, editing is blocked.
- All permissions are validated in the backend to prevent unauthorized access.

How to Run the Project:

1) pip install django
2) python manage.py migrate
3) python manage.py createsuperuser
4) python manage.py runserver
5) Open in browser
- http://127.0.0.1:8000/
  
Sample Credentials: 

Admin:
Username: admin
Password: admin123

Regular User:
Username: user1
Password: jasber123

What I Learned:

- How RBAC works in real applications
- How to design configurable permission systems
- Backend-level validation for security
- Handling dynamic UI rendering based on roles
- Designing clean role-permission mapping in database

Final Thoughts:

- This project helped me understand how enterprise-level applications manage access control in a scalable way. 
- Instead of relying on hardcoded checks, everything is driven through configuration, making it flexible and easier to maintain.
