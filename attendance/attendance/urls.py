"""
URL configuration for attendance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from student.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('' ,home ,name="home"),

    path('home/' ,home ,name="home"),

    path('index/' ,home ,name="home"),

# User Authentication

    path('login/' ,login_page ,name="login_page"),

    path('register/' ,register ,name="register"),

    path('delete-account/', delete_user, name='delete_account'),  

    path('logout/', logout_page, name='logout_page'),
    

# Attendance

    # Mark Attendance

    path('ceone/', ceone, name='ceone'),
    path('itmark/', itmark, name='itmark'),
    path('memark/', memark, name='memark'),
    path('cvmark/', cvmark, name='cvmark'),
    path('aemark/', aemark, name='aemark'),
    path('eemark/', eemark, name='eemark'),
    
    # Student List

    path('student-list/', student_list, name='student_list'),
    path('itstudent-list/', itstudent_list, name='itstudent_list'),
    path('mestudent-list/', mestudent_list, name='mestudent_list'),
    path('cvstudent-list/', cvstudent_list, name='cvstudent_list'),
    path('aestudent-list/', aestudent_list, name='aestudent_list'),
    path('eestudent-list/', eestudent_list, name='eestudent_list'),

    # Record Attendance

    path('cereport/', cereport, name='cereport'),
    path('itreport/', itreport, name='itreport'),
    path('mereport/', mereport, name='mereport'),
    path('cvreport/', cvreport, name='cvreport'),
    path('aereport/', aereport, name='aereport'),
    path('eereport/', eereport, name='eereport'),
    

    # Download Attendance CSV

    path('download_attendance_csv_ce/', download_attendance_csv_ce, name='download_attendance_csv_ce'),
    path('download_attendance_csv_ae/', download_attendance_csv_ae, name='download_attendance_csv_ae'),
    path('download_attendance_csv_me/', download_attendance_csv_me, name='download_attendance_csv_me'),
    path('download_attendance_csv_cv/', download_attendance_csv_cv, name='download_attendance_csv_cv'),
    path('download_attendance_csv_it/', download_attendance_csv_it, name='download_attendance_csv_it'),
    path('download_attendance_csv_ee/', download_attendance_csv_ee, name='download_attendance_csv_ee'),

    path('download_attendance_pdf_ce/', download_attendance_pdf_ce, name='download_attendance_pdf_ce'),
    path('download_attendance_pdf_ee/', download_attendance_pdf_ee, name='download_attendance_pdf_ee'),
    path('download_attendance_pdf_ae/', download_attendance_pdf_ae, name='download_attendance_pdf_ae'),
    path('download_attendance_pdf_cv/', download_attendance_pdf_cv, name='download_attendance_pdf_cv'),
    path('download_attendance_pdf_me/', download_attendance_pdf_me, name='download_attendance_pdf_me'),
    path('download_attendance_pdf_it/', download_attendance_pdf_it, name='download_attendance_pdf_it'),

    
]
