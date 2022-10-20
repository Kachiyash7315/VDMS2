from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from courses.models import Course, Video, UserCourse


# Create your views here.
def coursePage(request, slug):
    print(request.user.is_authenticated)
    course = Course.objects.get(slug=slug)
    serial_number = request.GET.get('lecture')
    if serial_number is None:
        serial_number = 1
    video = Video.objects.get(serial_number=serial_number, course=course)
    if video.is_preview is False:

        if request.user.is_authenticated is False:
            return redirect('login')
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user=user, course=course)
            except:
                return redirect('checkout', slug=course.slug)

    return render(request, template_name='courses/course_page.html', context={'course': course, 'video': video})


@login_required(login_url='login')
def mycourses(request):
    user = request.user
    user_courses = UserCourse.objects.filter(user=user)
    return render(request, template_name='courses/my_courses.html', context={'user_courses': user_courses})
