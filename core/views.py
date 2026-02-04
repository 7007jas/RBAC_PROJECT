from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django import forms
from .models import Employee, UserRole, Permission


# =========================
# Employee List View
# =========================
@login_required
def employee_list(request):
    user = request.user

    # If admin → show everything
    if user.is_superuser:
        employees = Employee.objects.all()
        return render(request, "employee_list.html", {
            "employees": employees,
            "show_salary": True
        })

    #  For normal users
    try:
        user_role = UserRole.objects.get(user=user)
    except UserRole.DoesNotExist:
        return HttpResponse("No role assigned")

    # Table-level view permission
    table_permission = Permission.objects.filter(
        role=user_role.role,
        table_name="Employee",
        field_name__isnull=True,
        can_view=True
    ).exists()

    if not table_permission:
        return HttpResponse("You don't have permission to view this table")

    # Field-level salary permission
    salary_permission = Permission.objects.filter(
        role=user_role.role,
        table_name="Employee",
        field_name="salary",
        can_view=True
    ).exists()

    employees = Employee.objects.all()

    return render(request, "employee_list.html", {
        "employees": employees,
        "show_salary": salary_permission
    })


# =========================
# Employee Form
# =========================
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'salary']


# =========================
# Edit Employee View
# =========================
@login_required
def edit_employee(request, emp_id):
    user = request.user

    employee = get_object_or_404(Employee, id=emp_id)

    #  If admin → allow directly
    if user.is_superuser:
        if request.method == "POST":
            form = EmployeeForm(request.POST, instance=employee)
            if form.is_valid():
                form.save()
                return redirect("employee_list")
        else:
            form = EmployeeForm(instance=employee)

        return render(request, "edit_employee.html", {"form": form})

    #  For normal users
    try:
        user_role = UserRole.objects.get(user=user)
    except UserRole.DoesNotExist:
        return HttpResponse("No role assigned")

    # Table-level edit permission
    edit_permission = Permission.objects.filter(
        role=user_role.role,
        table_name="Employee",
        field_name__isnull=True,
        can_edit=True
    ).exists()

    if not edit_permission:
        return HttpResponse("You don't have permission to edit")

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm(instance=employee)

    return render(request, "edit_employee.html", {"form": form})
