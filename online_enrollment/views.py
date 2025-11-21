from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Course, Section, Enrollment, AcademicRecord
from .forms import StudentForm, CourseForm, SectionForm, EnrollmentForm, AcademicRecordForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='studentLogin')
def addStudent(request):
    try:
        studentInfo = Student.objects.get(student = request.user)
    except Student.DoesNotExist:
        studentInfo = None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        studentInfo = None

    if request.method == "POST":
        print('Method is post')
        studentForm = StudentForm(request.POST, request.FILES)
        # courseForm = CourseForm()
        # sectionForm = SectionForm()
        # enrollmentForm = EnrollmentForm()
        academicRecordForm = AcademicRecordForm(request.POST)

        if studentForm.is_valid():
            studInstance = studentForm.save(commit=False)
            studInstance.student = request.user
            studInstance.save()

            messages.success(request, 'Record added')
            return redirect('dashboard')
        
        else:
            print(studentForm.errors)
    else:
        print('not post')
        studentForm = StudentForm()
        academicRecordForm = AcademicRecordForm()

    return render(request, 'addnew.html', {'studentForm' : studentForm,
                                            'studentInfo': studentInfo,
                                        #    'sectionForm': sectionForm,
                                        #    'enrollmentForm': enrollmentForm,
                                           'academicRecordForm':academicRecordForm
                                           })

# @login_required(login_url='studentLogin')
def dashboard(request):
    allStudent = Student.objects.all()
    try:
        studentInfo = Student.objects.get(student = request.user.is_authenticated)
    except Student.DoesNotExist:
        studentInfo = None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        studentInfo = None

    context = {
        'studentInfo': studentInfo,
        'allStudent':allStudent,
        'studentCount':  allStudent.count(),
        'pendingEnrollmentCount': Enrollment.objects.filter(status='P').count(),
        'activeCourseCount': Course.objects.filter(is_active=True).count(),
    }   
    return render(request, 'dashboard.html',context)

@login_required(login_url='studentLogin')
def profile(request):
    try:
        studentInfo = Student.objects.get(student = request.user)
    except Student.DoesNotExist:
        studentInfo = None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        studentInfo = None

    context = {
        'studentInfo' : studentInfo
    }
    
    return render(request, 'profile.html', context)


@login_required(login_url='studentLogin')
def editInfo(request):
    try:
        user = Student.objects.get(student = request.user)
    except Student.DoesNotExist:
        user = None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        user = None

    if request.method == "POST":
        print('naka psot nigga')
        studentForm = StudentForm(request.POST, request.FILES, instance=user)
        if studentForm.is_valid():

            studInstance = studentForm.save(commit=False)
            studInstance.student = request.user
            studInstance.save()

            messages.success(request, 'Edit successful')
            return redirect('profile')
        
        else:
            messages.error(request, 'Error, Please check your entries')
            print(studentForm.errors)
    else:
        print('tanga di naka post meth')
        studentForm = StudentForm(instance=user)

    context = {
        'studentForm': studentForm,
        'user': user
    }
    return render(request, 'editInfo.html', context)


def studentList(request):
    allStudent = Student.objects.all()
    return render(request, 'student-list.html', {'allStudent':allStudent})