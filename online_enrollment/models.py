from django.db import models
from django.contrib.auth.models import User

GENDERS = [
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
    ('OTHER', 'Other')
]
    
ENROLLMENT_STATUS = [
    ('P', 'Pending'),
    ('E', 'Enrolled'),
    ('D', 'Dropped')
]

class Student(models.Model):
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(choices=GENDERS, null=True, blank=True)
    def __str__(self):
        return f'ID: {self.student}, NAME: {self.firstName} {self.lastName}, EMAIL: {self.email}'
    
class Course(models.Model):
    course_code = models.CharField(max_length=100)
    course_title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    unit = models.IntegerField()
    is_active = models.BooleanField()

    def __str__(self):
        return f'COURSE ID: {self.id}, COURSE CODE: {self.course_code}, COURSE TITLE {self.course_title}, UNIT: {self.unit}, ACTIVE: {self.is_active}'
    
class Section(models.Model):
    start_end_time = models.CharField(max_length=100)
    days_of_week = models.CharField(max_length=100)
    room_number = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return f'SECTION ID: {self.id}, TIME: {self.start_end_time}, DAYS: {self.days_of_week}, ROOM: {self.room_number}, INSTRUCTOR: {self.instructor}'

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)
    grade = models.IntegerField(null=True, blank=True)
    status = models.CharField(choices=ENROLLMENT_STATUS, default='Pending')

    def __str__(self):
        return f'ENROLLMENT ID: {self.enrollment_id}, STUDENT ID: {self.student_id}, DATE: {self.enrollment_date}, GRADE: {self.grade}, STATUS: {self.status}'

class AcademicRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_units_earned = models.IntegerField()
    gpa = models.DecimalField(decimal_places=2, max_digits=10)
    graduation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'RECORD ID: {self.id}, STUDENT ID: {self.student_id}, UNITS: {self.total_units_earned}, GPA: {self.gpa}, GRADUATIONS DATE: {self.graduation_date}'