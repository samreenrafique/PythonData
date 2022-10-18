from django.shortcuts import render
from crudapp.models import Employee


def showData(request):
    emp = Employee.objects.all()
    return render(request, "ShowData.html",{'emps':emp})
