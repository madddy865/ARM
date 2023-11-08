"""
URL configuration for project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from app2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', views.registration_view, name="registration"),
    path('', views.home_view, name="home"),
    path('attendance/', views.Attendance_view, name="attendance"),
    path('about/', views.about_view, name="about"),
    path('cd/', views.coursedetails_view, name="coursedetails"),
    path('sd/', views.Student_details_view, name="student_details"),
    path('Ad/', views.Attendance_details_view, name="attendance_details"),
    path('login/', views.Login_view, name="login"),
    path('loginmain/', views.loginmain_view, name="loginmain"),
    path('studentPassword/', views.StudentPassword, name="studentPassword"),
    path('studentLogin/', views.StdLogin_view, name="studentlogin"),
]


