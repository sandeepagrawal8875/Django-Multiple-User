from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from users.views import HomeListView, TeacherSignUpView, StudentSignUpView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('account/signup/student', StudentSignUpView.as_view(), name='student_signup' ),
    path('account/signup/teacher', TeacherSignUpView.as_view(), name='teacher_signup' ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)