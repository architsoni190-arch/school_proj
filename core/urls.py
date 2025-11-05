from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('parents/', views.parent_list, name='parent_list'),
]
