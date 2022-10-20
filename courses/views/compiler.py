from django.shortcuts import render


def java(request):
    return render(request, template_name="courses/java.html")


def python(request):
    return render(request, template_name="courses/python.html")


def cpp(request):
    return render(request, template_name="courses/cpp.html")


def sql(request):
    return render(request, template_name="courses/sql.html")
