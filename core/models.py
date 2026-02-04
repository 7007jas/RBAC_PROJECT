from django.db import models


# Employee Table
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


# Project Table
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.title

from django.contrib.auth.models import User


# Role Table
class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Assign Role to User
class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.role.name}"


# Permission Configuration
class Permission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    table_name = models.CharField(max_length=100)  # Employee or Project
    field_name = models.CharField(max_length=100, blank=True, null=True)  # Column name
    can_view = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.role.name} - {self.table_name} - {self.field_name}"
