from .models import Student, Course, Section, Enrollment, AcademicRecord
from django.forms import ModelForm
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter student email'}),
        } 

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'

        widgets = {
            'enrollment_date': forms.DateInput(attrs={'type': 'date'}),
        }

class AcademicRecordForm(forms.ModelForm):
    class Meta:
        model = AcademicRecord
        fields = '__all__'
        widgets = {
            'graduation_date': forms.DateInput(attrs={'type': 'date'}),
        }