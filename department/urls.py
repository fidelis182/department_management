from django.contrib import admin
from django.urls import path,include

from department import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("courses/", views.courses, name="courses"),
    path("trainer/", views.trainer, name="trainer"),
    path("announcements/", views.announcements, name="announcements"),
]