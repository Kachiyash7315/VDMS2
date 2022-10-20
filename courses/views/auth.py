from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from courses.forms.registration_form import RegistrationForm
from courses.forms.login_form import loginForm
from django.views import View

from django.views.generic.edit import FormView


class SignUpView(FormView):
    template_name = 'courses/signup.html'
    form_class = RegistrationForm
    success_url = '/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


'''
class SignUpView(View):
    def get(self, request):
        if request.method == 'GET':
            form = RegistrationForm()
            return render(request, template_name='courses/signup.html', context={'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
        return render(request, template_name='courses/signup.html', context={'form': form})
'''


# class LoginView(FormView):
#     template_name = 'courses/signup.html'
#     form_class = loginForm
#     success_url = '/'
#
#     def form_valid(self, form):
#
#         return super().form_valid(form)

class LoginView(View):
    def get(self, request):
        form = loginForm()
        return render(request, template_name='login.html', context={'form': form})

    def post(self, request):
        form = loginForm(request=request, data=request.POST)
        if form.is_valid():
            return redirect('home')
        return render(request, template_name='login.html', context={'form': form})


def signout(request):
    logout(request)
    return redirect('home')
