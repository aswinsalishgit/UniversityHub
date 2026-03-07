from django.urls import path
from academic import views

urlpatterns = [
    #path('students/', views.student_list),

    #path(route, view, name)
    path('hello/', views.hello_world),
    path('courses/', views.course_list),
    path("register-student/", views.student_create, name="student_create"),
]