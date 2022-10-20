from django.http import HttpResponse
from django.shortcuts import render

from courses.models import Course


# Create your views here.
def home(request):
    courses = Course.objects.filter(active=True)
    print(courses)
    return render(request, template_name='courses/home.html', context={'courses': courses})


def main(request):
    print("Hello")
    return render(request, template_name='courses/main.html')


def internship(request):
    return render(request, template_name='courses/internship.html')
