from django.urls import path
from . import views

urlpatterns = [
    path("employees/", views.employee_list, name="employee_list"),
    path("employees/edit/<int:emp_id>/", views.edit_employee, name="edit_employee"),

]
