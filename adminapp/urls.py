from django.contrib import admin
from django.urls import path
from adminapp.views import *
from adminapp import views

from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('register_Student/', views.StudentRegistrationView.as_view(), name='register-student'),
    path('register_parent/', views.ParentRegistrationView.as_view(), name='register-parent'),

    path('register_Teacher/', views.TeacherRegistrationView.as_view(), name='register-teacher'),
    path('view_teachers/', views.ViewTeacher.as_view(), name='view-teacher'),
    path('teacher_detail/<int:teacher_id>/', views.TeacherDetail.as_view(), name='teacher-detail'),
    path('view_students/', views.ViewStudent.as_view(), name='view-student'),
    path('student_detail/<int:student_id>/', views.StudentDetail.as_view(), name='student-detail'),
    
    path('add-Article/', views.AddArticleView.as_view() , name = "add-Article"), #for authenticated users
    path('view-Article/', views.ListArticleView.as_view() , name = "view-Article"), #for all users
    path('detail-article/<str:slug>/',views.ArticleDetail.as_view(), name='detail-article'),
    

    # path('',views.dashboard , name = 'dashboard'),
    # path('Add_Teacher', views.Add_Teacher.as_view() , name = "Add_Teacher"),
    # path('Add_Student', views.Add_Student.as_view() , name = "Add_Student"),
    path('Assign_Course', views.Assign_Course.as_view() , name = "Assign_Course"),
    path('Enroll_Student', views.Enroll_Student.as_view() , name = "'Enroll_Student'"),
    path('Add_Course', views.Add_Course.as_view() , name = "Add_Course"),
    # path('View_Teacher', views.View_Teacher.as_view() , name = "View_Teacher"),
    path('View_Course', views.View_Course.as_view() , name = "View_Course"),
    path('CourseDetail/<str:slug>/', views.CourseDetail.as_view() , name = "Course"),
    # path('Delete_Course/<str:slug>/', views.Delete_Course.as_view() , name = "Delete_Course"),
    path('Unassign_Course/<int:assign_course_id>/', views.Unassign_Course.as_view() , name = "Unassign_Course"),
    path('Add_Class', views.Add_Class.as_view() , name = "Add_Class"),
    path('View_Class', views.View_Class.as_view() , name = "View_Class"),

    # ************************* Memoona Update *******************************
    path('Edit_Class/<str:slug>/', views.Edit_Class.as_view() , name = "Edit_Class"),
    path('Delete_Class/<str:slug>/', views.Delete_Class.as_view() , name = "Delete_Class"),
    path('Add_Section', views.Add_Section.as_view() , name = "Add_Section"),
    path('View_Section', views.View_Section.as_view() , name = "View_Section"),
    path('Edit_Section/<str:slug>/', views.Edit_Section.as_view() , name = "Edit_Section"),
    path('Delete_Section/<str:slug>/', views.Delete_Section.as_view() , name = "Delete_Section"),
    path('schools/', views.SchoolsView.as_view(), name='view-school'),
    path('school_detail/<int:school_id>/', views.SchoolDetail.as_view(), name='school-detail'),
    # ************************* Memoona Update *******************************
    
    path('Class_Detail/<str:slug>/', views.Class_Detail.as_view() , name = "Edit_Class"),
    # path('Modify_Teacher/<str:slug>/' , views.Modify_Teacher.as_view() , name = 'Modify_Teacher'),
    # path('Modify_Student/<str:slug>/' , views.Modify_Student.as_view() , name = 'Modify_Student'),
    # path('Delete_Teacher/<str:slug>/' , views.Delete_Teacher.as_view() , name = 'Delete_Teacher'),
    # path('Delete_Student/<str:slug>/' , views.Delete_Student.as_view() , name = 'Delete_Student'),
    path('feedback' , views.feedback.as_view() , name = 'feedback'),
    
    path('ViewRespondedQueries', views.ViewRespondedQueries.as_view(), name = 'View_Responded_Queries'),
    path('ViewUnRespondedQueries', views.ViewUnRespondedQueries.as_view(), name = 'View_UnRespoded_Queries'),
    path('Respond_Queries/<int:pk>/', views.Respond_Queries.as_view(), name = 'Respond_Queries'),

    path('role', views.Role.as_view(), name='role'),
    path('Admin_info/', views.AdminProfileView.as_view(), name="Admin-info"),

    path('add_Announcement', views.AddAnnouncementView.as_view(), name='add_Announcement'), #post
    path('view_Announcement', views.ListAnnouncementView.as_view(), name='view_Announcements'), #get
    path('Announcement_detail', views.AnnouncementDetailView.as_view(), name='Announcement_detail'), 
    path('delete_update_Announcement<str:slug>/',views.AnnouncementDeleteUpdateView.as_view(), name='update_delete_Announcement'),

    ]

urlpatterns = format_suffix_patterns(urlpatterns)