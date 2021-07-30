from django.contrib import admin
from django.urls import path
from client.views import *
from client import views
from django.conf.urls import url, include

urlpatterns = [
    path('register_client/', views.ClientRegistrationView.as_view(), name='register-client'),

    path('enrolled_courses/<int:course_id>/<int:client_id>', views.Enroll_CourseView.as_view(), name = 'viewEnrolledCourses'),
    path('Detailenrolled_courses/<int:pk>', views.DetailCourse_EnrollView.as_view(), name = 'EnrolledCourses'),
    
    path('add-Article/', views.AddArticleView.as_view() , name = "add-Article"), #for authenticated users
    path('view-Article/', views.ListArticleView.as_view() , name = "view-Article"), #for all users
    path('detail-article/<str:slug>/',views.ArticleDetail.as_view(), name='detail-article'),
    
    path('view_Announcement', views.View_Annnouncement.as_view(), name='view_Announcements'), #get
    path('Announcement_detail', views.DetailView_Announcement.as_view(), name='Announcement_detail'), 

    path('submit_feedback/<int:course_id>', views.ViewAndSubmitFeedback.as_view(), name='submitFeedback'),
   
   path('submit_complain', views.ViewAndSubmitFeedback.as_view(), name='submitFeedback'),
    
    
    
    
    path('Client_info/', views.ClientProfileView.as_view(), name="Client-info")
]
