from .models import Student, Course, Section, Enrollment, AcademicRecord
from django.forms import ModelForm
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter student email'}),
            'firstName': forms.TextInput(attrs={'placeholder': 'e.g. Ronjerick'}),
            'lastName': forms.TextInput(attrs={'placeholder': 'e.g. Gamba'}),
            'age': forms.TextInput(attrs={'placeholder': 'e.g. 27'}),
            'address': forms.TextInput(attrs={'placeholder': 'e.g. Dalahican Desert'}),
            'studentIdentifier': forms.TextInput(attrs={'placeholder': 'e.g. 023A-10900'}),
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
            'total_units_earned': forms.TextInput(attrs={'placeholder': 'e.g. 3.0'}),
            'gpa': forms.TextInput(attrs={'placeholder': 'e.g. 1'}),
        }