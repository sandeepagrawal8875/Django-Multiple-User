from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required

from .models import User, Profile
from .forms import StudentSignUpForm, TeacherSignUpForm


class HomeListView(ListView):
    model = Profile
    context_object_name = 'profile_list'
    template_name = 'home.html'


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/student_signup.html'

    def form_valid(self, form):
        user = form.save()
        return redirect('login')


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/teacher_signup.html'
    
    def form_valid(self, form):
        user = form.save()
        print(user)
        login(self.request, user)
        return redirect('login')
    