from django.db import models

class Parent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Student(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='students')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)

    def __str__(self):
        return self.name
