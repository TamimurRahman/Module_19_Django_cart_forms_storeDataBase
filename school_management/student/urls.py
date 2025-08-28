from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/',views.home,name='home'),#This is for function based view
    path('home/',views.StudentLists.as_view(),name='home'), #This is for class based view
    # path('create/',views.create,name='create_student'), #function based view
     path('create/',views.createStudent.as_view(),name='create_student'), #class based view
    # path('update/<int:id>/',views.update_student,name ='update_student'),#This is the function based view
    path('update/<int:id>/',views.UpdateStudentData.as_view(),name ='update_student'),# This is the class based view
    # path('delete/<int:id>/',views.delete_student,name= 'delete_student'), # function based view
    path('delete/<int:id>/',views.deleteStudent.as_view(),name= 'delete_student'), # class based view
]


    