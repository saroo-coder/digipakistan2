from django.contrib import admin
from django.urls import path
from superadmin.views import *
from superadmin import views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('register_school/', views.SchoolRegistrationView.as_view(), name='register-school'),
    # Tested
    path('add-course/', views.AddCourses.as_view() , name = "add-course"),
    path('view-course/', views.ViewCourse.as_view() , name = "view-course"),
    path('course/<str:slug>/', views.CourseDetailView.as_view() , name = "course-detail"),
    path('delete_update_course<str:slug>/',views.CourseDeleteUpdateView.as_view(), name='update_delete_course'),
   
    path('Enroll_Course', views.Enroll_Course.as_view() , name = "'Enroll_Course'"),#post
    path('view_Enroll_Course/<int:course_id>/<int:client_id>', views.ViewEnroll_Course.as_view(), name='view_EnrollCourse'), #get
    path('Enroll_Course_detail/<int:pk>/', views.DetailEnroll_CourseView.as_view(), name='EnrollCourse_detail'), 

    path('add-question/', views.AddQuestions.as_view() , name = "add-question"),
    path('view-question/', views.ViewQuestion.as_view() , name = "view-question"),
    path('question/<str:slug>/', views.QuestionDetailView.as_view() , name = "question-detail"),
    path('delete_update_question<str:slug>/',views.QuestionDeleteUpdateView.as_view(), name='update_delete_question'),

    #Done and tested
    path('add-Article/', views.AddArticleView.as_view() , name = "add-Article"), #for authenticated users
    path('view-Article/', views.ListArticleView.as_view() , name = "view-Article"), #for all users
     path('detail-article/<str:slug>/',views.ArticleDetail.as_view(), name='detail-article'),
    # (put,patch,delete : for superadmin only, superadmin can update status or approve articles from this endpoint)
    path('delete_update_Article/<str:slug>/',views.ArticleDeleteUpdate.as_view(), name='update_delete_Article'),

    path('add-question/', views.Add_question.as_view() , name = "add-question"),
    path('view-question/<int:course_id>', views.Viewquestion.as_view() , name = "view-question"),
    path('question/<int:pk>/', views.QuestionDetail.as_view() , name = "question-detail"),
     
    path('add-onlinetest/', views.AddonlineTest.as_view() , name = "add-test"), 
    path('view-OnlineTest/<int:course_id>', views.ViewOnlinetest.as_view() , name = "view-test"),
    path('OnlineTest/<int:pk>/', views.onlinetestDetail.as_view() , name = "question-test"),
    path('submitted_test/<int:course_id>/<int:client_id>' , views.SubmittedonlineTestView.as_view(), name='submitted_test'),
    path('submitted_questionTest/<int:course_id>/<int:client_id>' , views.SubmittedQuestionView.as_view(), name='submitted_questions'),

    #Done
    
    path('add-School/', views.AddSchools.as_view() , name = "add-School"),
    path('view-School/', views.ViewSchool.as_view() , name = "view-School"),
    path('School/<str:slug>/', views.SchoolDetailView.as_view() , name = "School-detail"),
    path('delete_update_School<str:slug>/',views.SchoolDeleteUpdateView.as_view(), name='update_delete_School'),

    # path('add-Blog/', views.AddBlogs.as_view() , name = "add-Blog"),
    # path('view-Blog/', views.ViewBlog.as_view() , name = "view-Blog"),
    # path('Blog/<str:slug>/', views.BlogDetailView.as_view() , name = "Blog-detail"),
    # path('delete_update_Blog<str:slug>/',views.BlogDeleteUpdateView.as_view(), name='update_delete_Blog'),

    # Tested
    path('add-event/', views.AddEventView.as_view() , name = "add-event"),
    path('lits-event/', views.ListEventView.as_view() , name = "list-event"),
    path('event/<str:slug>/', views.EventDetailView.as_view() , name = "event_detail"),
    path('delete_update_event/<str:slug>/',views.EventDeleteUpdateView.as_view(), name='update_delete_event'),
    

    # Tested
    path('add-BusinessPartner/', views.AddBusinessPartners.as_view() , name = "add-BusinessPartner"),
    path('view-BusinessPartner/', views.ViewBusinessPartner.as_view() , name = "view-BusinessPartner"),
    path('BusinessPartner/<str:slug>/', views.BusinessPartnerDetailView.as_view() , name = "BusinessPartner-detail"),
    path('delete_update_BusinessPartner<str:slug>/',views.BusinessPartnerDeleteUpdateView.as_view(), name='update_delete_BusinessPartner'),

    # Done and tested
    path('add-KidStory/', views.AddKidStory.as_view() , name = "add-KidStory"),
    path('view-KidStory/', views.ViewKidStory.as_view() , name = "view-KidStory"),
    path('KidStory/<str:slug>/', views.KidStoryDetailView.as_view() , name = "KidStory-detail"),
    path('delete_update_KidStory/<str:slug>/',views.KidStoryDeleteUpdateView.as_view(), name='update_delete_KidStory'),

    # Done and tested
    path('add-KidTalent/', views.AddKidTalent.as_view() , name = "add-KidTalent"),
    path('view-KidTalent/', views.ViewKidTalent.as_view() , name = "view-KidTalent"),
    path('KidTalent/<str:slug>/', views.KidTalentDetailView.as_view() , name = "KidTalent-detail"),
    path('delete_update_KidTalent/<str:slug>/',views.KidTalentDeleteUpdateView.as_view(), name='update_delete_KidTalent'),

    path('add-QuizContext/', views.AddQuizContext.as_view() , name = "add-QuizContext"),
    path('view-QuizContext/', views.ViewQuizContext.as_view() , name = "view-QuizContext"),
    path('QuizContext/<str:slug>/', views.QuizContextDetailView.as_view() , name = "QuizContext-detail"),
    path('delete_update_QuizContext<str:slug>/',views.QuizContextDeleteUpdateView.as_view(), name='update_delete_QuizContext'),
    
    path('add-Feedback/', views.AddFeedback.as_view() , name = "add-Feedback"),
    path('view-Feedback/', views.ViewFeedback.as_view() , name = "view-Feedback"),
    path('Feedback/<str:slug>/', views.FeedbackDetailView.as_view() , name = "Feedback-detail"),
    path('delete_update_Feedback<str:slug>/',views.FeedbackDeleteUpdateView.as_view(), name='update_delete_Feedback'),
    
    # Tested
    path('add-WebsiteAd/', views.AddWebsiteAd.as_view() , name = "add-WebsiteAd"),
    path('view-WebsiteAd/', views.ViewWebsiteAd.as_view() , name = "view-WebsiteAd"),
    path('WebsiteAd/<str:slug>/', views.WebsiteAdDetailView.as_view() , name = "WebsiteAd-detail"),
    path('delete_update_WebsiteAd<str:slug>/',views.WebsiteAdDeleteUpdateView.as_view(), name='update_delete_WebsiteAd'),
    
    # path('add-Approval/', views.AddApproval.as_view() , name = "add-Approval"),
    # path('view-Approval/', views.ViewApproval.as_view() , name = "view-Approval"),
    # path('Approval/<str:slug>/', views.ApprovalDetailView.as_view() , name = "Approval-detail"),
    # path('delete_update_Approval<str:slug>/',views.ApprovalDeleteUpdateView.as_view(), name='update_delete_Approval'),

    # Tested
    path('add-BusinessPromotion/', views.AddBusinessPromotion.as_view() , name = "add-BusinessPromotion"),
    path('view-BusinessPromotion/', views.ViewBusinessPromotion.as_view() , name = "view-BusinessPromotion"),
    path('BusinessPromotion/<str:slug>/', views.BusinessPromotionDetailView.as_view() , name = "BusinessPromotion-detail"),
    path('delete_update_BusinessPromotion<str:slug>/',views.BusinessPromotionDeleteUpdateView.as_view(), name='update_delete_BusinessPromotion'),

    # Tested (but some confusions)
    path('add-Team/', views.AddTeam.as_view() , name = "add-Team"),
    path('view-Team/', views.ViewTeam.as_view() , name = "view-Team"),
    path('Team/<str:slug>/', views.TeamDetailView.as_view() , name = "Team-detail"),
    path('delete_update_Team<str:slug>/',views.TeamDeleteUpdateView.as_view(), name='update_delete_Team'),

    # Tested
    path('add-AdvisoryBoard/', views.AddAdvisoryBoard.as_view() , name = "add-AdvisoryBoard"),
    path('view-AdvisoryBoard/', views.ViewAdvisoryBoard.as_view() , name = "view-AdvisoryBoard"),
    path('AdvisoryBoard/<str:slug>/', views.AdvisoryBoardDetailView.as_view() , name = "AdvisoryBoard-detail"),
    path('delete_update_AdvisoryBoard<str:slug>/',views.AdvisoryBoardDeleteUpdateView.as_view(), name='update_delete_AdvisoryBoard'),

    # Tested
    path('add_announcement/',  views.AddAnnouncement.as_view() , name = "announcement"),
    path('list_announcements/',  views.ListAnnouncement.as_view() , name = "list_announcement"),
    path('announcements/<str:slug>/',  views.AnnouncementDetail.as_view() , name = "announcement_detail"),
    path('delete_update_Announcement/<str:slug>/',views.AnnouncementDeleteUpdate.as_view(), name='update_delete_Announcement'),

    # Tested
    path('add-JobClassified/', views.AddJobClassified.as_view() , name = "add-JobClassified"),
    path('view-JobClassified/', views.ViewJobClassified.as_view() , name = "view-JobClassified"),
    path('JobClassified/<str:slug>/', views.JobClassifiedDetailView.as_view() , name = "JobClassified-detail"),
    path('delete_update_JobClassified<str:slug>/',views.JobClassifiedDeleteUpdateView.as_view(), name='update_delete_JobClassified'),

    # Todo : model change
    path('add-CustomerReview/', views.AddCustomerReviews.as_view() , name = "add-CustomerReview"),
    path('view-CustomerReview/', views.ViewCustomerReview.as_view() , name = "view-CustomerReview"),
    path('CustomerReview/<str:slug>/', views.CustomerReviewDetailView.as_view() , name = "CustomerReview-detail"),
    path('delete_update_CustomerReview<str:slug>/',views.CustomerReviewDeleteUpdateView.as_view(), name='update_delete_CustomerReview'),

    # Tested
    path('SuperAdmin_info/', views.SuperadminProfileView.as_view(), name="superadmin-info"),

    

]
