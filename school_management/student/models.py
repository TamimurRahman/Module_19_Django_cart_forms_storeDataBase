from django.db import models
import os
def student_directory_name(instance,filename):
    return os.path.join('student/media',instance.name,filename)
class student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(unique=False)
    email = models.EmailField()
    phone = models.CharField(max_length = 15)
    age = models.IntegerField()
    photo = models.ImageField(upload_to=student_directory_name,default=None,null=True)
    password = models.CharField(max_length=100)
    checkbox = models.BooleanField(default=False)
    
    def __str__(self):
        return f"ID: {self.id} | Name: {self.name}"