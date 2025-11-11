from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Student
from .forms import StudentForm

# List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})

# Create a new student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'core/student_form.html', {'form': form, 'title': 'Add Student'})

# Update an existing student
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'core/student_form.html', {'form': form, 'title': 'Edit Student'})

# Delete a student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'core/student_confirm_delete.html', {'student': student})

#-------------******----- queries implementation------*******----------------

from django.shortcuts import render             # Used to render HTML templates
from django.db.models import Q                  # Used for complex queries (like OR conditions)
from .models import Student                     # Import the Student model from current app
def student_list(request):
    # Start by fetching all student records from the database
    students = Student.objects.all()
    name = request.GET.get('name')                    # e.g. /students?name=Hemish
    age_gt = request.GET.get('age_greater_than')      # e.g. /students?age_greater_than=18
    age_lt = request.GET.get('age_less_than')         # e.g. /students?age_less_than=15
    grade = request.GET.get('grade')                  # e.g. /students?grade=10
    search = request.GET.get('search')                # e.g. /students?search=hem
    if name:
        students = students.filter(name__icontains=name)  # "icontains" → means "contains", ignoring case
    if age_gt:
        students = students.filter(age__gte=age_gt)   # Filter by age greater than or equal to a value
    if age_lt:
        students = students.filter(age__lte=age_lt)  # Filter by age less than or equal to a value
    if grade:
        students = students.filter(grade__iexact=grade) # Filter by grade (exact match but case-insensitive)

   # USING Q OBJECT FOR COMPLEX FILTERS
    if search:
        students = students.filter(
            Q(name__icontains=search) | Q(grade__icontains=search)
        )
    return render(request, 'core/student_list.html', {'students': students})