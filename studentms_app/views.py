from django.shortcuts import render, redirect
from .models import Student, Course, Enrollment


# show all students
def student_list(request):
    students = Student.objects.all()
    enrollments = Enrollment.objects.all()

    return render(request, 'student_list.html', {
        'students': students,
        'enrollments': enrollments
    })



# add a new student
def add_student(request):
    courses = Course.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        admission_date = request.POST.get('admission_date')
        course_id = request.POST.get('course')

        if not course_id:
            return render(request, 'add_student.html', {
                'courses': courses,
                'error': 'Please select a course'
            })

        student = Student.objects.create(
            name=name,
            email=email,
            phone=phone,
            admission_date=admission_date
        )

        course = Course.objects.get(id=course_id)

        Enrollment.objects.create(
            student=student,
            course=course
        )

        return render(request, 'admission_success.html')

    return render(request, 'add_student.html', {'courses': courses})




# edit student
def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.roll_number = request.POST.get('roll_number')
        student.email = request.POST.get('email')
        student.department = request.POST.get('department')
        student.admission_date = request.POST.get('admission_date')
        student.save()

        return redirect('student_list')

    return render(request, 'edit_student.html', {'student': student})


# delete student
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')


# show all courses
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course_code = request.POST.get('course_code')
        credit_hours = request.POST.get('credit_hours')

        Course.objects.create(
            course_name=course_name,
            course_code=course_code,
            credit_hours=credit_hours
        )

        return redirect('course_list')

    return render(request, 'add_course.html')

def delete_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'delete_student.html', {'student': student})
