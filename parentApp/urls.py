from django.contrib import admin
from django.urls import path
from parentApp.views import *
from parentApp import views

from django.conf.urls import url, include

urlpatterns = [
    path('enrolled_courses', views.ViewEnrolledCourses.as_view(), name = 'viewEnrolledCourses'),
    path('announcement/<int:course_id>/<int:class_id>', views.ViewAnnoucement.as_view(), name = "announcement"),
    path('submit_feedback/<int:course_id>/<int:class_id>', views.ViewAndSubmitFeedback.as_view(), name='submitFeedback'),

    
]
