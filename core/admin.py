from django.contrib import admin
from .models import Employee, Project, Role, UserRole, Permission

admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Role)
admin.site.register(UserRole)
admin.site.register(Permission)
