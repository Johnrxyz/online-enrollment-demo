from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Course, Section, Enrollment, AcademicRecord
from .forms import StudentForm, CourseForm, SectionForm, EnrollmentForm, AcademicRecordForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
def addStudent(request):
    if request.method == "POST":
        studentForm = StudentForm(request.POST)
        # courseForm = CourseForm()
        # sectionForm = SectionForm()
        # enrollmentForm = EnrollmentForm()
        # academicRecordForm = AcademicRecordForm()

        if studentForm.is_valid():
            studInstance = studentForm.save(commit=False)
            studInstance.student = request.user
            studInstance.save()

            messages.success(request, 'Record added')
            return redirect('dashboard')
        
        else:
            print(studentForm.errors)
    else:
        studentForm = StudentForm()

    return render(request, 'addnew.html', {'studentForm' : studentForm,
                                        #    'courseForm': courseForm,
                                        #    'sectionForm': sectionForm,
                                        #    'enrollmentForm': enrollmentForm,
                                        #    'academicRecordForm':academicRecordForm
                                           })

@login_required(login_url='login')
def dashboard(request):
    try:
        studentInfo = Student.objects.get(student = request.user)
    except:
        studentInfo = False

    context = {
        'studentInfo' : studentInfo
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def editInfo(request):
    user = Student.objects.get(student = request.user)
    if request.method == "POST":
        print('naka psot nigga')
        studentForm = StudentForm(request.POST, instance=user)
        if studentForm.is_valid():

            studInstance = studentForm.save(commit=False)
            studInstance.student = request.user
            studInstance.save()

            messages.success(request, 'Edit successful')
            return redirect('dashboard')
        
        else:
            messages.error(request, 'Error, Please check your entries')
            print(studentForm.errors)
    else:
        print('tanga di naka post meth')
        studentForm = StudentForm(instance=user)

    context = {
        'studentForm': studentForm
    }
    return render(request, 'editInfo.html', context)