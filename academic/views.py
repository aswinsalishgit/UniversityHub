from tkinter.tix import Form
from urllib import request

from django.shortcuts import HttpResponse

from .models import Course
#def student_list(request):
    #return HttpResponse("List of Students")

def hello_world(request):
    # This returns raw text, not HTML
    return HttpResponse("Welcome to University Hub!")

from django.shortcuts import render
from.models import Course
def course_list(request):
    #1. Fetch data from DB
    all_courses = Course.objects.all()
    # 2. Context: A dictionary mapping template variable names to Python objects
    context = {
        'courses': all_courses,
        'page_title': 'Available Courses'
    }
    #3. Render: Combine the request, the template, and the data
    return render (request, 'academic/course_list.html', context)


from.forms import Student, StudentForm

def student_create(request):
    
    if request.method == 'POST':
        #1. Bind data to the form
        form = StudentForm(request.POST)

        #2. Validation Check
        if form.is_valid():
            #3. Save to DB
            form.save()
            #4. Redirect (Post-Redirect-Get Pattern) return redirect('course_list')

    else:
        #GET request: Create empty form
        form = StudentForm()

    return render(request,
                'academic/student_form.html',
                {'form': form})