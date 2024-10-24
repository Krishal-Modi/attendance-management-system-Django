from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.models import *
from .forms import *
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
# Create your views here.


def home(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return redirect('/register/')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        messages.info(request, 'Account created successfully')
        return redirect('/login/')

    return render(request, 'register.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home/')  # Redirect to home page upon successful login
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('/login/')

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')



def delete_user(request):
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            user.delete()
            logout(request)  # Log the user out after deletion
            messages.success(request, "Your account has been deleted successfully.")
            return redirect('login_page')  # Redirect to login after account deletion

    return redirect('home')  # Redirect to home if accessed directly





# Computer Engineering Department


def ceone(request):
    students = Student.objects.all()
    distinct_dates = StudentAttendance.objects.order_by().values('date').distinct()

    if request.method == 'POST':
        username = request.POST.get('username')
        date = request.POST.get('date')
        time = request.POST.get('time')

        for student in students:
            status = request.POST.get(f"attendance_{student.id}")
            if status in ['absent', 'present']:
                StudentAttendance.objects.update_or_create(
                    student=student, date=date,
                    defaults={'status': status, 'time': time, 'username': username}
                )
        return redirect(reverse("home"))
    else:
        form = AttendanceForm()
    
    student_attendance = {student.id: {att.date: att for att in StudentAttendance.objects.filter(student=student)} for student in students}
    
    return render(request, "ceone.html", {
        'form': form,
        'students': students,
        'distinct_dates': [d['date'] for d in distinct_dates],
        'student_attendance': student_attendance,
    })



def student_list(request):
    # Retrieve all students from the database
    students = Student.objects.all()
    # Pass the list of students to the template for rendering
    return render(request, 'ceone.html', {'students': students})


# Appearing the Result of the student
def get_student_attendance(student, distinct_dates):
    attendance_records = {}
    for date in distinct_dates:
        attendance = student.studentattendance_set.filter(date=date).first()
        attendance_records[date] = attendance.status if attendance else ''
    return attendance_records


def cereport(request):
    students = Student.objects.all()
    distinct_dates = StudentAttendance.objects.values_list('date', flat=True).distinct()

    # Prepare attendance records for each student and date
    student_attendance = {}
    for student in students:
        attendance_records = StudentAttendance.objects.filter(student=student)
        attendance_data = {}
        for record in attendance_records:
            attendance_data[record.date] = {
                'status': record.status,
                'time': record.time,
                'username': record.username
            }
        student_attendance[student.id] = attendance_data
    
    return render(request, 'cereport.html', {
        'students': students,
        'distinct_dates': distinct_dates,
        'student_attendance': student_attendance,
    })



# Information Technology Department


def get_student_attendance(student, distinct_dates):
    attendance_records = {}
    for date in distinct_dates:
        attendance = student.studentattendance_set.filter(date=date).first()
        attendance_records[date] = attendance.status if attendance else ''
    return attendance_records


def itmark(request):
    students = Studentit.objects.all()
    distinct_dates = StudentAttendanceit.objects.order_by().values('date').distinct()

    if request.method == 'POST':
        username = request.POST.get('username')
        date = request.POST.get('date')
        time = request.POST.get('time')

        for student in students:
            status = request.POST.get(f"attendance_{student.id}")
            if status in ['absent', 'present']:
                StudentAttendanceit.objects.update_or_create(
                    student=student, date=date,
                    defaults={'status': status, 'time': time, 'username': username}
                )
        return redirect(reverse("home"))
    else:
        form = AttendanceForm()
    
    student_attendance = {student.id: {att.date: att for att in StudentAttendanceit.objects.filter(student=student)} for student in students}
    
    return render(request, "itmark.html", {
        'form': form,
        'students': students,
        'distinct_dates': [d['date'] for d in distinct_dates],
        'student_attendance': student_attendance,
    })


def itstudent_list(request):
    students = Studentit.objects.all()
    return render(request, 'itmark.html', {'students': students})


def itreport(request):
    students = Studentit.objects.all()
    distinct_dates = StudentAttendanceit.objects.values_list('date', flat=True).distinct()

    # Prepare attendance records for each student and date
    student_attendance = {}
    for student in students:
        attendance_records = StudentAttendanceit.objects.filter(student=student)
        attendance_data = {}
        for record in attendance_records:
            attendance_data[record.date] = {
                'status': record.status,
                'time': record.time,
                'username': record.username
            }
        student_attendance[student.id] = attendance_data
    
    return render(request, 'itreport.html', {
        'students': students,
        'distinct_dates': distinct_dates,
        'student_attendance': student_attendance,
    })


# Mechanical Engineering


def get_student_attendance(student, distinct_dates):
    attendance_records = {}
    for date in distinct_dates:
        attendance = student.studentattendance_set.filter(date=date).first()
        attendance_records[date] = attendance.status if attendance else ''
    return attendance_records


def memark(request):
    students = Studentme.objects.all()
    distinct_dates = StudentAttendanceme.objects.order_by().values('date').distinct()

    if request.method == 'POST':
        username = request.POST.get('username')
        date = request.POST.get('date')
        time = request.POST.get('time')

        for student in students:
            status = request.POST.get(f"attendance_{student.id}")
            if status in ['absent', 'present']:
                StudentAttendanceme.objects.update_or_create(
                    student=student, date=date,
                    defaults={'status': status, 'time': time, 'username': username}
                )
        return redirect(reverse("home"))
    else:
        form = AttendanceForm()
    
    student_attendance = {student.id: {att.date: att for att in StudentAttendanceme.objects.filter(student=student)} for student in students}
    
    return render(request, "memark.html", {
        'form': form,
        'students': students,
        'distinct_dates': [d['date'] for d in distinct_dates],
        'student_attendance': student_attendance,
    })


def mestudent_list(request):
    students = Studentme.objects.all()
    return render(request, 'memark.html', {'students': students})


def mereport(request):
    students = Studentme.objects.all()
    distinct_dates = StudentAttendanceme.objects.values_list('date', flat=True).distinct()

    # Prepare attendance records for each student and date
    student_attendance = {}
    for student in students:
        attendance_records = StudentAttendanceme.objects.filter(student=student)
        attendance_data = {}
        for record in attendance_records:
            attendance_data[record.date] = {
                'status': record.status,
                'time': record.time,
                'username': record.username
            }
        student_attendance[student.id] = attendance_data
    
    return render(request, 'mereport.html', {
        'students': students,
        'distinct_dates': distinct_dates,
        'student_attendance': student_attendance,
    })


# Civil Engineering


def get_student_attendance(student, distinct_dates):
    attendance_records = {}
    for date in distinct_dates:
        attendance = student.studentattendance_set.filter(date=date).first()
        attendance_records[date] = attendance.status if attendance else ''
    return attendance_records


def cvmark(request):
    students = Studentcv.objects.all()
    distinct_dates = StudentAttendancecv.objects.order_by().values('date').distinct()

    if request.method == 'POST':
        username = request.POST.get('username')
        date = request.POST.get('date')
        time = request.POST.get('time')

        for student in students:
            status = request.POST.get(f"attendance_{student.id}")
            if status in ['absent', 'present']:
                StudentAttendancecv.objects.update_or_create(
                    student=student, date=date,
                    defaults={'status': status, 'time': time, 'username': username}
                )
        return redirect(reverse("home"))
    else:
        form = AttendanceForm()
    
    student_attendance = {student.id: {att.date: att for att in StudentAttendancecv.objects.filter(student=student)} for student in students}
    
    return render(request, "cvmark.html", {
        'form': form,
        'students': students,
        'distinct_dates': [d['date'] for d in distinct_dates],
        'student_attendance': student_attendance,
    })


def cvstudent_list(request):
    students = Studentcv.objects.all()
    return render(request, 'cvmark.html', {'students': students})


def cvreport(request):
    students = Studentcv.objects.all()
    distinct_dates = StudentAttendancecv.objects.values_list('date', flat=True).distinct()

    # Prepare attendance records for each student and date
    student_attendance = {}
    for student in students:
        attendance_records = StudentAttendancecv.objects.filter(student=student)
        attendance_data = {}
        for record in attendance_records:
            attendance_data[record.date] = {
                'status': record.status,
                'time': record.time,
                'username': record.username
            }
        student_attendance[student.id] = attendance_data
    
    return render(request, 'cvreport.html', {
        'students': students,
        'distinct_dates': distinct_dates,
        'student_attendance': student_attendance,
    })


# Aeronautical Engineering


def get_student_attendance(student, distinct_dates):
    attendance_records = {}
    for date in distinct_dates:
        attendance = student.studentattendance_set.filter(date=date).first()
        attendance_records[date] = attendance.status if attendance else ''
    return attendance_records


def aemark(request):
    students = Studentae.objects.all()
    distinct_dates = StudentAttendanceae.objects.order_by().values('date').distinct()

    if request.method == 'POST':
        username = request.POST.get('username')
        date = request.POST.get('date')
        time = request.POST.get('time')

        for student in students:
            status = request.POST.get(f"attendance_{student.id}")
            if status in ['absent', 'present']:
                StudentAttendanceae.objects.update_or_create(
                    student=student, date=date,
                    defaults={'status': status, 'time': time, 'username': username}
                )
        return redirect(reverse("home"))
    else:
        form = AttendanceForm()
    
    student_attendance = {student.id: {att.date: att for att in StudentAttendanceae.objects.filter(student=student)} for student in students}
    
    return render(request, "aemark.html", {
        'form': form,
        'students': students,
        'distinct_dates': [d['date'] for d in distinct_dates],
        'student_attendance': student_attendance,
    })


def aestudent_list(request):
    students = Studentae.objects.all()
    return render(request, 'aemark.html', {'students': students})


def aereport(request):
    students = Studentae.objects.all()
    distinct_dates = StudentAttendanceae.objects.values_list('date', flat=True).distinct()

    # Prepare attendance records for each student and date
    student_attendance = {}
    for student in students:
        attendance_records = StudentAttendanceae.objects.filter(student=student)
        attendance_data = {}
        for record in attendance_records:
            attendance_data[record.date] = {
                'status': record.status,
                'time': record.time,
                'username': record.username
            }
        student_attendance[student.id] = attendance_data
    
    return render(request, 'aereport.html', {
        'students': students,
        'distinct_dates': distinct_dates,
        'student_attendance': student_attendance,
    })


# Electrical Engineering


def get_student_attendance(student, distinct_dates):
    attendance_records = {}
    for date in distinct_dates:
        attendance = student.studentattendance_set.filter(date=date).first()
        attendance_records[date] = attendance.status if attendance else ''
    return attendance_records


def eemark(request):
    students = Studentee.objects.all()
    distinct_dates = StudentAttendanceee.objects.order_by().values('date').distinct()

    if request.method == 'POST':
        username = request.POST.get('username')
        date = request.POST.get('date')
        time = request.POST.get('time')

        for student in students:
            status = request.POST.get(f"attendance_{student.id}")
            if status in ['absent', 'present']:
                StudentAttendanceee.objects.update_or_create(
                    student=student, date=date,
                    defaults={'status': status, 'time': time, 'username': username}
                )
        return redirect(reverse("home"))
    else:
        form = AttendanceForm()
    
    student_attendance = {student.id: {att.date: att for att in StudentAttendanceee.objects.filter(student=student)} for student in students}
    
    return render(request, "eemark.html", {
        'form': form,
        'students': students,
        'distinct_dates': [d['date'] for d in distinct_dates],
        'student_attendance': student_attendance,
    })


def eestudent_list(request):
    students = Studentee.objects.all()
    return render(request, 'eemark.html', {'students': students})


def eereport(request):
    students = Studentee.objects.all()
    distinct_dates = StudentAttendanceee.objects.values_list('date', flat=True).distinct()

    # Prepare attendance records for each student and date
    student_attendance = {}
    for student in students:
        attendance_records = StudentAttendanceee.objects.filter(student=student)
        attendance_data = {}
        for record in attendance_records:
            attendance_data[record.date] = {
                'status': record.status,
                'time': record.time,
                'username': record.username
            }
        student_attendance[student.id] = attendance_data
    
    return render(request, 'eereport.html', {
        'students': students,
        'distinct_dates': distinct_dates,
        'student_attendance': student_attendance,
    })  



# For CSV Download

import csv


# CSV Download For Computer Engineering Department

def download_attendance_csv_ce(request):
    students = Student.objects.all()
    distinct_dates = StudentAttendance.objects.values_list('date', flat=True).distinct()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendance_report.csv"'

    # Create a CSV writer object
    writer = csv.writer(response)

    # Write the CSV header (columns)
    header = ['Student ID', 'Student Name'] + [str(date) for date in distinct_dates]
    writer.writerow(header)

    # Write the attendance data for each student
    for student in students:
        row = [student.id, student.name]  # Start the row with student ID and name

        # Add the attendance status for each date
        for date in distinct_dates:
            attendance = StudentAttendance.objects.filter(student=student, date=date).first()
            status = attendance.status if attendance else 'Absent'
            row.append(status)

        # Write the row to the CSV
        writer.writerow(row)

    return response


# CSV Download For Auronatical Engineering Department

def download_attendance_csv_ae(request):
    students = Studentae.objects.all()
    distinct_dates = StudentAttendanceae.objects.values_list('date', flat=True).distinct()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendance_report.csv"'

    # Create a CSV writer object
    writer = csv.writer(response)

    # Write the CSV header (columns)
    header = ['Student ID', 'Student Name'] + [str(date) for date in distinct_dates]
    writer.writerow(header)

    # Write the attendance data for each student
    for student in students:
        row = [student.id, student.name]  # Start the row with student ID and name

        # Add the attendance status for each date
        for date in distinct_dates:
            attendance = StudentAttendanceae.objects.filter(student=student, date=date).first()
            status = attendance.status if attendance else 'Absent'
            row.append(status)

        # Write the row to the CSV
        writer.writerow(row)

    return response


# CSV Download For Civil Engineering Department

def download_attendance_csv_cv(request):
    students = Studentcv.objects.all()
    distinct_dates = StudentAttendancecv.objects.values_list('date', flat=True).distinct()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendance_report.csv"'

    # Create a CSV writer object
    writer = csv.writer(response)

    # Write the CSV header (columns)
    header = ['Student ID', 'Student Name'] + [str(date) for date in distinct_dates]
    writer.writerow(header)

    # Write the attendance data for each student
    for student in students:
        row = [student.id, student.name]  # Start the row with student ID and name

        # Add the attendance status for each date
        for date in distinct_dates:
            attendance = StudentAttendancecv.objects.filter(student=student, date=date).first()
            status = attendance.status if attendance else 'Absent'
            row.append(status)

        # Write the row to the CSV
        writer.writerow(row)

    return response


# CSV Download For Electrical Engineering Department

def download_attendance_csv_ee(request):
    students = Studentee.objects.all()
    distinct_dates = StudentAttendanceee.objects.values_list('date', flat=True).distinct()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendance_report.csv"'

    # Create a CSV writer object
    writer = csv.writer(response)

    # Write the CSV header (columns)
    header = ['Student ID', 'Student Name'] + [str(date) for date in distinct_dates]
    writer.writerow(header)

    # Write the attendance data for each student
    for student in students:
        row = [student.id, student.name]  # Start the row with student ID and name

        # Add the attendance status for each date
        for date in distinct_dates:
            attendance = StudentAttendanceee.objects.filter(student=student, date=date).first()
            status = attendance.status if attendance else 'Absent'
            row.append(status)

        # Write the row to the CSV
        writer.writerow(row)

    return response


# CSV Download For Information Technology Department

def download_attendance_csv_it(request):
    students = Studentit.objects.all()
    distinct_dates = StudentAttendanceit.objects.values_list('date', flat=True).distinct()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendance_report.csv"'

    # Create a CSV writer object
    writer = csv.writer(response)

    # Write the CSV header (columns)
    header = ['Student ID', 'Student Name'] + [str(date) for date in distinct_dates]
    writer.writerow(header)

    # Write the attendance data for each student
    for student in students:
        row = [student.id, student.name]  # Start the row with student ID and name

        # Add the attendance status for each date
        for date in distinct_dates:
            attendance = StudentAttendanceit.objects.filter(student=student, date=date).first()
            status = attendance.status if attendance else 'Absent'
            row.append(status)

        # Write the row to the CSV
        writer.writerow(row)

    return response


# CSV Download For Mechanical Engineering Department

def download_attendance_csv_me(request):
    students = Studentme.objects.all()
    distinct_dates = StudentAttendanceme.objects.values_list('date', flat=True).distinct()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendance_report.csv"'

    # Create a CSV writer object
    writer = csv.writer(response)

    # Write the CSV header (columns)
    header = ['Student ID', 'Student Name'] + [str(date) for date in distinct_dates]
    writer.writerow(header)

    # Write the attendance data for each student
    for student in students:
        row = [student.id, student.name]  # Start the row with student ID and name

        # Add the attendance status for each date
        for date in distinct_dates:
            attendance = StudentAttendanceme.objects.filter(student=student, date=date).first()
            status = attendance.status if attendance else 'Absent'
            row.append(status)

        # Write the row to the CSV
        writer.writerow(row)

    return response


############ PDF Download 

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.http import HttpResponse
from reportlab.lib import colors

# PDF Download For Computer Engineering Department


def download_attendance_pdf_ce(request):
    students = Student.objects.all()
    distinct_dates = StudentAttendance.objects.values_list('date', flat=True).distinct()

    # Create the HttpResponse object with the appropriate PDF header
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="attendance_report.pdf"'

    # Create a SimpleDocTemplate with the PDF response as the destination
    doc = SimpleDocTemplate(response, pagesize=letter)

    # Data for the table
    table_data = []
    
    # Add header row to the table
    header = ["Student ID", "Student Name"] + [str(date) for date in distinct_dates]
    table_data.append(header)

    # Add rows for each student
    for student in students:
        row = [str(student.id), student.name]  # Start with ID and Name
        
        for date in distinct_dates:
            attendance = StudentAttendance.objects.filter(student=student, date=date).first()
            status = attendance.status if attendance else 'Absent'
            row.append(status)  # Add status for each date
            
        table_data.append(row)

    # Create the table
    table = Table(table_data)

    # Define the table style for borders, alignment, and colors
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add grid lines
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),  # Set font
        ('FONTSIZE', (0, 0), (-1, -1), 10),  # Set font size for all cells
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Add padding below header
        ('TOPPADDING', (0, 0), (-1, -1), 5),  # Add padding to all rows
    ]))

    # Build the PDF with the table
    elements = [table]
    doc.build(elements)

    return response


# PDF Download For Information Technology Department


def download_attendance_pdf_it(request):
    students = Studentit.objects.all()
    distinct_dates = StudentAttendanceit.objects.values_list('date', flat=True).distinct()

    # Create the HttpResponse object with the appropriate PDF header
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="attendance_report.pdf"'

    # Create a SimpleDocTemplate with the PDF response as the destination
    doc = SimpleDocTemplate(response, pagesize=letter)

    # Data for the table
    table_data = []
    
    # Add header row to the table
    header = ["Student ID", "Student Name"] + [str(date) for date in distinct_dates]
    table_data.append(header)

    # Add rows for each student
    for student in students:
        row = [str(student.id), student.name]  # Start with ID and Name
        
        for date in distinct_dates:
            attendance = StudentAttendanceit.objects.filter(student=student, date=date).first()
            status = attendance.status if attendance else 'Absent'
            row.append(status)  # Add status for each date
            
        table_data.append(row)

    # Create the table
    table = Table(table_data)

    # Define the table style for borders, alignment, and colors
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add grid lines
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),  # Set font
        ('FONTSIZE', (0, 0), (-1, -1), 10),  # Set font size for all cells
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Add padding below header
        ('TOPPADDING', (0, 0), (-1, -1), 5),  # Add padding to all rows
    ]))

    # Build the PDF with the table
    elements = [table]
    doc.build(elements)

    return response


# PDF Download For Mechanical Engineering Department


def download_attendance_pdf_me(request):
    students = Studentme.objects.all()
    distinct_dates = StudentAttendanceme.objects.values_list('date', flat=True).distinct()

    # Create the HttpResponse object with the appropriate PDF header
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="attendance_report.pdf"'

    # Create a SimpleDocTemplate with the PDF response as the destination
    doc = SimpleDocTemplate(response, pagesize=letter)

    # Data for the table
    table_data = []
    
    # Add header row to the table
    header = ["Student ID", "Student Name"] + [str(date) for date in distinct_dates]
    table_data.append(header)

    # Add rows for each student
    for student in students:
        row = [str(student.id), student.name]  # Start with ID and Name
        
        for date in distinct_dates:
            attendance = StudentAttendanceme.objects.filter(student=student, date=date).first()
            status = attendance.status if attendance else 'Absent'
            row.append(status)  # Add status for each date
            
        table_data.append(row)

    # Create the table
    table = Table(table_data)

    # Define the table style for borders, alignment, and colors
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add grid lines
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),  # Set font
        ('FONTSIZE', (0, 0), (-1, -1), 10),  # Set font size for all cells
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Add padding below header
        ('TOPPADDING', (0, 0), (-1, -1), 5),  # Add padding to all rows
    ]))

    # Build the PDF with the table
    elements = [table]
    doc.build(elements)

    return response


# PDF Download For Civil Engineering Department


def download_attendance_pdf_cv(request):
    students = Studentcv.objects.all()
    distinct_dates = StudentAttendancecv.objects.values_list('date', flat=True).distinct()

    # Create the HttpResponse object with the appropriate PDF header
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="attendance_report.pdf"'

    # Create a SimpleDocTemplate with the PDF response as the destination
    doc = SimpleDocTemplate(response, pagesize=letter)

    # Data for the table
    table_data = []
    
    # Add header row to the table
    header = ["Student ID", "Student Name"] + [str(date) for date in distinct_dates]
    table_data.append(header)

    # Add rows for each student
    for student in students:
        row = [str(student.id), student.name]  # Start with ID and Name
        
        for date in distinct_dates:
            attendance = StudentAttendancecv.objects.filter(student=student, date=date).first()
            status = attendance.status if attendance else 'Absent'
            row.append(status)  # Add status for each date
            
        table_data.append(row)

    # Create the table
    table = Table(table_data)

    # Define the table style for borders, alignment, and colors
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add grid lines
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),  # Set font
        ('FONTSIZE', (0, 0), (-1, -1), 10),  # Set font size for all cells
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Add padding below header
        ('TOPPADDING', (0, 0), (-1, -1), 5),  # Add padding to all rows
    ]))

    # Build the PDF with the table
    elements = [table]
    doc.build(elements)

    return response


# PDF Download For Auronatical Engineering Department


def download_attendance_pdf_ae(request):
    students = Studentae.objects.all()
    distinct_dates = StudentAttendanceae.objects.values_list('date', flat=True).distinct()

    # Create the HttpResponse object with the appropriate PDF header
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="attendance_report.pdf"'

    # Create a SimpleDocTemplate with the PDF response as the destination
    doc = SimpleDocTemplate(response, pagesize=letter)

    # Data for the table
    table_data = []
    
    # Add header row to the table
    header = ["Student ID", "Student Name"] + [str(date) for date in distinct_dates]
    table_data.append(header)

    # Add rows for each student
    for student in students:
        row = [str(student.id), student.name]  # Start with ID and Name
        
        for date in distinct_dates:
            attendance = StudentAttendanceae.objects.filter(student=student, date=date).first()
            status = attendance.status if attendance else 'Absent'
            row.append(status)  # Add status for each date
            
        table_data.append(row)

    # Create the table
    table = Table(table_data)

    # Define the table style for borders, alignment, and colors
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add grid lines
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),  # Set font
        ('FONTSIZE', (0, 0), (-1, -1), 10),  # Set font size for all cells
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Add padding below header
        ('TOPPADDING', (0, 0), (-1, -1), 5),  # Add padding to all rows
    ]))

    # Build the PDF with the table
    elements = [table]
    doc.build(elements)

    return response


# PDF Download For Electrical Engineering Department


def download_attendance_pdf_ee(request):
    students = Studentee.objects.all()
    distinct_dates = StudentAttendanceee.objects.values_list('date', flat=True).distinct()

    # Create the HttpResponse object with the appropriate PDF header
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="attendance_report.pdf"'

    # Create a SimpleDocTemplate with the PDF response as the destination
    doc = SimpleDocTemplate(response, pagesize=letter)

    # Data for the table
    table_data = []
    
    # Add header row to the table
    header = ["Student ID", "Student Name"] + [str(date) for date in distinct_dates]
    table_data.append(header)

    # Add rows for each student
    for student in students:
        row = [str(student.id), student.name]  # Start with ID and Name
        
        for date in distinct_dates:
            attendance = StudentAttendanceee.objects.filter(student=student, date=date).first()
            status = attendance.status if attendance else 'Absent'
            row.append(status)  # Add status for each date
            
        table_data.append(row)

    # Create the table
    table = Table(table_data)

    # Define the table style for borders, alignment, and colors
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add grid lines
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),  # Set font
        ('FONTSIZE', (0, 0), (-1, -1), 10),  # Set font size for all cells
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Add padding below header
        ('TOPPADDING', (0, 0), (-1, -1), 5),  # Add padding to all rows
    ]))

    # Build the PDF with the table
    elements = [table]
    doc.build(elements)

    return response