"""
URL configuration for online_courses_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from courses import views as course_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', course_views.home, name='home'),
    path('courses/', course_views.course_list, name='course_list'),
    path('courses/<int:course_id>/', course_views.course_detail, name='course_detail'),
    path('profile/', course_views.profile, name='profile'),
    path('enroll/<int:course_id>/', course_views.enroll_course, name='enroll_course'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', course_views.register, name='register'),
    path('login/', course_views.login_view, name='login'),
]