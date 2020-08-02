from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Profile
  

class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        profile = Profile.objects.create(user=user)
        profile.save()
        return user
    
class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
        profile = Profile.objects.create(user=user)
        profile.save()
        return user