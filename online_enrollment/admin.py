from django.contrib import admin
from .models import Student, Course, Section, Enrollment, AcademicRecord, ApparelStyle, SizeMeasurements, MeasurementUnit
# Register your models here.

admin.site.register([Student, Course, Section, Enrollment, AcademicRecord, ApparelStyle, SizeMeasurements, MeasurementUnit]) 
