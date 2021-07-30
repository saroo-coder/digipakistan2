
from django.contrib import admin
from django.urls import path
from teacherApp.views import *
from teacherApp import views

from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

    path('view_courses_and_classes', views.ViewAssignedCoursesAndClass.as_view(), name="view-classes"),


    path('add_attendance', views.AddStudentAttendanceView.as_view(), name='add_attendance'), #post
    path('view_attendance/<int:course_id>/<int:class_id>', views.ViewAttendance.as_view(), name='view_Attendance'), #get
    path('Attendance_detail/<int:pk>/', views.DetailStudentAttendanceView.as_view(), name='Attendance_Detail'),

    path('Add_announcement', views.AddAnnouncementView.as_view(), name = "announcement"),
    path('announcement_detail/<int:pk>/', views.DetailAnnouncementView.as_view(), name = "announcement"),
    path('announcement/<int:course_id>/<int:class_id>', views.AnnouncementView.as_view(), name = "announcement"),
    
   
    path('assignment/<int:course_id>/<int:class_id>', views.AddAssignment.as_view() , name = "addAssignmnet"),
    #get update delete
    path('detail_assignment/<str:slug>/', views.DetailAssignment.as_view(), name = "deleteAssignmnet"),

   

    path('lecture', views.AddLecture.as_view(), name = "lecture"), #post
    path('list_lecture_course_wise/<int:course_id>/<int:class_id>', #get
        views.ListLectureCourseWise.as_view(), name = "list-lecture" 
        ),
    path('lecture_detail/<str:slug>/', views.LectureDetail.as_view(), name = "lecture_detail"), #get, put, delete

    path('feedback/<int:course_id>/<int:class_id>', views.Feedback.as_view(), name = "feedback"), #get
    path('feedback_detail/<int:pk>/', views.FeedbackDetail.as_view(), name = "feedback_detail"), #get

    path('discussion/<int:course_id>/<int:class_id>', views.Discussion.as_view(), name = "discussion"), #get
    #teacher and student both can use this endpoint
    path('ans_discussion_detail/<str:slug>/', views.AnsDiscussion.as_view(), name = "discussion_detail"), #post

    path('add_calender', views.AddCalender.as_view(), name='add_calender'), #post
    #get
    path('view_calender/<int:course_id>/<int:class_id>', views.ViewCalender.as_view(), name='view_calender'),
    path('calender_detail/<str:slug>/', views.CalenderDetail.as_view(), name='del_cal'), #get, put, delete

    
    path('add_Quiz', views.AddQuiz.as_view(), name='add_Quiz'), #post
    #get
    path('view_Quiz/<int:course_id>/<int:class_id>', views.ViewQuiz.as_view(), name='view_Quiz'),
    path('Quiz_detail/<str:slug>/', views.QuizDetail.as_view(), name='del_Quiz'),

    path('add_Question', views.AddQuestion.as_view(), name='add_Question'), #post
    #get
    path('view_Question/<int:course_id>/<int:class_id>', views.ViewQuestion.as_view(), name='view_Question'),
    path('Question_detail/<str:slug>/', views.QuestionDetail.as_view(), name='del_cal'),

    path('add_test', views.Addtest.as_view(), name='add_test'), #post
    #get
    path('view_test/<int:course_id>/<int:class_id>', views.Viewtest.as_view(), name='view_test'),
    path('test_detail/<str:slug>/', views.testDetail.as_view(), name='del_test'), #get, put, delete

    path('add_result', views.AddResultView.as_view(), name='add_result'), #post
    path('view_result/<int:course_id>/<int:class_id>', views.ViewResults.as_view(), name='view_results'), #get
    path('result_detail/<int:pk>/', views.DetailResultView.as_view(), name='result_detail'), 

    path('add-Article/', views.AddArticleView.as_view() , name = "add-Article"), #for authenticated users
    path('view-Article/', views.ListArticleView.as_view() , name = "view-Article"), #for all users
    path('detail-article/<str:slug>/',views.ArticleDetail.as_view(), name='detail-article'),
    
    # path('submitted_assignment' , views.SubmittedAssignmentView.as_view(), name='submitted_assignment'),


   
   
    



    path('submitted_assignment/<int:course_id>/<int:class_id>' , views.SubmittedAssignmentView.as_view(), name='submitted_assignment'),
    path('Teacher_info/', views.TeacherProfileView.as_view(), name="Teacher-info")
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
