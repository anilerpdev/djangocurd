from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Student
from .forms import StudentForm


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})


def save_student_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            students = Student.objects.all()
            data['html_student_list'] = render_to_string('students/includes/partial_student_list.html', {
                'students': students
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
    else:
        form = StudentForm()
    return save_student_form(request, form, 'students/includes/partial_student_create.html')


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
    else:
        form = StudentForm(instance=student)
    return save_student_form(request, form, 'students/includes/partial_student_update.html')


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    data = dict()
    if request.method == 'POST':
        student.delete()
        data['form_is_valid'] = True
        students = Student.objects.all()
        data['html_student_list'] = render_to_string('students/includes/partial_student_list.html', {
            'students': students
        })
    else:
        context = {'student': student}
        data['html_form'] = render_to_string('students/includes/partial_student_delete.html', context, request=request)
    return JsonResponse(data)
