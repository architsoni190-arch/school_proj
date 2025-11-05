from django.shortcuts import render
from .models import Student, Parent

def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})

def parent_list(request):
    parents = Parent.objects.all()
    return render(request, 'core/parent_list.html', {'parents': parents})
