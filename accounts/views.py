from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from .models import Profile
import random

import http.client

from django.conf import settings
from django.contrib.auth import authenticate, login

# Create your views here.
from django.conf import settings
import http.client


def send_otp(mobile, otp):
    # print("FUNCTION CALLED")
    # conn = http.client.HTTPSConnection("api.msg91.com")
    # authkey = settings.API_KEY
    # print(authkey)
    # headers = {'content-type': "application/json"}
    # url = 'http://control.msg91.com/api/sendotp.php?otp=' + otp + '&sender=ABC&message=' + 'Your otp is ' + otp + '&mobile=' + mobile + '&authkey=' + authkey + '&country=+91'
    # url = url.replace(" ", "%20")
    # conn.request("GET", url, headers=headers)
    # res = conn.getresponse()
    # data = res.read()
    # print(data)
    # return None
    conn = http.client.HTTPSConnection("api.msg91.com")

    payload = "{\"Value1\":\"Param1\",\"Value2\":\"Param2\",\"Value3\":\"Param3\"}"

    headers = {'Content-Type': "application/json"}

    conn.request("GET", "/api/v5/otp?template_id=&mobile=9552182322&authkey=381747AULNlwx4EIIS631743d4P1", payload,
                 headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


@login_required
def cart(request):
    print("Hello")
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        # check_user = User.objects.filter(email=email).first()
        usereg = Profile(name=name, email=email, mobile=Profile.mobile, otp=Profile.otp)
        usereg.save()
        print(usereg.name)

        print("User saved successfully")
        return redirect('registeruser')
    return render(request, 'cart.html')


def login_attempt(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')

        user = Profile.objects.filter(mobile=mobile).first()

        if user is None:
            context = {'message': 'User not found', 'class': 'danger'}
            return render(request, 'login.html')

        otp = str(random.randint(1000, 9999))
        user.otp = otp
        user.save()
        send_otp(mobile, otp)
        request.session['mobile'] = mobile
        return redirect('login_otp')
    return render(request, 'login.html')


def login_otp(request):
    mobile = request.session['mobile']
    context = {'mobile': mobile}
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Profile.objects.filter(mobile=mobile).first()

        if otp == profile.otp:
            # user = User.objects.get(id=profile.user.id)
            # login(request, user)
            return redirect('cart')
        else:
            context = {'message': 'Wrong OTP', 'class': 'danger', 'mobile': mobile}
            return render(request, 'login_otp.html', context)

    return render(request, 'login_otp.html', context)


def register(request):
    if request.method == 'POST':
        # email = request.POST.get('email')
        # name = request.POST.get('name')
        mobile = request.POST.get('mobile')

        # check_user = User.objects.filter(email=email).first()
        check_profile = Profile.objects.filter(mobile=mobile).first()

        if check_profile:
            context = {'message': 'User already exists', 'class': 'danger'}
            return render(request, 'register.html', context)

        otp = str(random.randint(1000, 9999))
        profile = Profile(mobile=mobile, otp=otp)
        profile.save()
        send_otp(mobile, otp)
        request.session['mobile'] = mobile
        return redirect('otp')
    return render(request, 'register.html')


def registeruser(request):
    print("Hello")
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        # check_user = User.objects.filter(email=email).first()
        usereg = Profile(name=name, email=email)
        usereg.save()
        print(usereg.name)

        print("User saved successfully")
        return redirect('registeruser')
    return render(request, 'register.html')


def otp(request):
    mobile = request.session['mobile']
    context = {'mobile': mobile}
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Profile.objects.filter(mobile=mobile).first()

        if otp == profile.otp:
            return redirect('cart')
        else:
            print('Wrong')

            context = {'message': 'Wrong OTP', 'class': 'danger', 'mobile': mobile}
            return render(request, 'otp.html', context)

    return render(request, 'otp.html', context)
