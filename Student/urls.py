from django.contrib import admin
from django.urls import path
from . import views

from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # path('assignment/<slug>', views.ShowAssignment.as_view(), name = 'showAssignment')
    #get request
    path('enrolled_courses', views.ViewEnrolledCourses.as_view(), name = 'viewEnrolledCourses'),
    #get request
    path('view_assignments/<int:course_id>/<int:class_id>', views.ViewAssignment.as_view(), name = 'viewAssignment'),
    #get or post request
    path('submit_assignment/<int:assignment_id>', views.SubmitAssignment.as_view(), name = 'submitAssignment'),
    #post and get
    path('submit_feedback/<int:course_id>/<int:class_id>', views.ViewAndSubmitFeedback.as_view(), name='submitFeedback'),
    #get
    path('view_lectures/<int:course_id>/<int:class_id>', views.ViewLectures.as_view(), name='viewLectures'),
    #get
    path('lecture_detail/<int:course_id>/<int:class_id>/<int:lecture_id>', views.LectureDetail.as_view(), name='lectureDetail'),
      #get
    path('view_result/<int:course_id>/<int:class_id>', views.ViewResults.as_view(), name='viewResults'),
    path('view_Notes/<int:teacher_id>', views.ViewNotes.as_view(), name='viewNotes'),

    #post
    path('post_query/<int:course_id>/<int:class_id>', views.DiscussionForm.as_view(), name='discussionForm'),
    #get
    path('view_queries/<int:course_id>/<int:class_id>', views.ListDiscussion.as_view(), name='listDiscussion'),
    #post
    path('submit_complain', views.SubmitComplain.as_view(), name='submitComplain'),
    path('view_complain', views.ViewComplain.as_view(), name='viewComplain'),

    path('view_tests/<int:course_id>/<int:class_id>', views.ViewTest.as_view(), name = 'viewtest'),
    #get or post request
    path('submit_test/<int:test_id>', views.Submittest.as_view(), name = 'submittest'),


    path('view_questions/<int:course_id>/<int:class_id>', views.ViewQuestion.as_view(), name = 'viewquestion'),
    #get or post request
    path('submit_question/<int:question_id>', views.Submitquestion.as_view(), name = 'submitquestion'),

    path('view_calender/<int:course_id>/<int:class_id>', views.ViewCalender.as_view(), name='viewCalender'), #get
    path('calender_detail/<str:slug>/', views.CalenderDetail.as_view(), name='detailCalender'), #get
    path('view_result/<int:course_id>/<int:class_id>', views.ViewResults.as_view(), name='viewResults'), #get
    path('result_detail/<int:pk>/', views.DetailResultView.as_view(), name='resultDetail'),

    path('add-Article/', views.AddArticleView.as_view() , name = "add-Article"), #for authenticated users
    path('view-Article/', views.ListArticleView.as_view() , name = "view-Article"), #for all users
    path('detail-article/<str:slug>/',views.ArticleDetail.as_view(), name='detail-article'),
    
    path('view_attendance/<int:course_id>/<int:class_id>', views.ViewAttendance.as_view(), name='viewAttendance'), #get
    path('attendance_detail/<int:pk>/', views.DetailAttendanceView.as_view(), name='AttendanceDetail'),
    
    path('announcement_detail/<int:pk>/', views.DetailAnnouncementView.as_view(), name = "announcement"),
    path('announcement/<int:course_id>/<int:class_id>', views.ViewAnnoucement.as_view(), name = "announcement"),
   
    
    path('Student_info/', views.StudentProfileView.as_view(), name="student-info")
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)