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