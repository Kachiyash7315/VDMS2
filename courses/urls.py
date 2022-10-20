from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.views import *
from . import views
from django.contrib.auth import views as auth_views
from .views import homepage, courses, auth, checkout, compiler
from OTP_Verification.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('home', homepage.home, name='home'),
    path('', homepage.main, name='main'),
    path('course/<str:slug>', courses.coursePage, name='coursepage'),
    path('checkout/<str:slug>', checkout.checkout2, name='checkout'),
    path('verify_payment', checkout.verifyPayment, name='verify_payment'),
    path('signup', auth.SignUpView.as_view(), name='signup'),
    path('login', auth.LoginView.as_view(), name='login'),
    path('reset_password_complete/login', auth.LoginView.as_view(), name='login'),

    path('logout', auth.signout, name='logout'),
    path('mycourses', courses.mycourses, name='mycourses'),
    path('java', compiler.java, name='java'),
    path('python', compiler.python, name='python'),
    path('cpp', compiler.cpp, name='cpp'),
    path('sql', compiler.sql, name='sql'),
    path('internship',homepage.internship,name='internship'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="courses/password_reset.html"), name="reset_password"),
path('reset_password_send/',auth_views.PasswordResetDoneView.as_view(template_name="courses/password_reset_sent.html"), name="password_reset_done"),
path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="courses/password_reset_form"
                                                                                         ".html"),
     name="password_reset_confirm"),
path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="courses"
                                                                                           "/password_reset_done.html") ,name="password_reset_complete"),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
