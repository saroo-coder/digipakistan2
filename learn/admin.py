from django.contrib import admin
from .models import AdvisorayBoard, Article, BusinessOfferType, Bank, ArticleType, QuizContextResult
from .models import WebAdd
from .models import WebSiteReview
from .models import HelpCategory
from .models import Subscribers
from .models import Donar
from .models import BusinessOffer
from .models import BlogType
from .models import Section
from .models import RoleName
from .models import Category
from .models import Answer
from .models import Status
from .models import CertificateType
from .models import ClientMessage
from .models import ClientReply
from .models import Collaborations
from .models import TblClass
from .models import School
from .models import Day
from .models import Department
from .models import DepartmentBoard
from .models import Replies
from .models import Event
from .models import SuperAdmin
from .models import Exam
from .models import TranscationType
from .models import Student
from .models import Course
from .models import Teacher
from .models import SchoolAssignment
from .models import Announcement
from .models import ArticleComments
from .models import AssignmentResult
from .models import Blog
from .models import Client
from .models import Certificate
from .models import ClientSchoolComplain
from .models import ClientCertificate
from .models import Comments
from .models import CourseAssignToTeacher
from .models import Discussion
from .models import Help
from .models import KidsStoryType
from .models import KidsStory
from .models import KidTalent
from .models import Lecture
from .models import Login
from .models import ManualTest
from .models import Messages
from .models import Question
from .models import OnlineTest
from .models import OnlineTestAnswers
from .models import OnlineTestQuestionOption
from .models import OnlineTestResults
from .models import Options
from .models import PaymentConfirmation
from .models import Post
from .models import QuizContext
from .models import ResultClient
from .models import StudentComplain
from .models import StudentHistory
from .models import StudentMaster
from .models import StudentResult
from .models import SubmitManualTest
from .models import Team
from .models import TechnicTip
from .models import TimeTable
from .models import UserEnrollInCourse
from .models import UserFeedBack
from .models import Attendance
from .models import Calender
from .models import Parents
from .models import SubmitAssignment
# header
admin.site.site_header = "Let's Learn Digitally Admin"
# Register your models here.

admin.site.register(SubmitAssignment)
admin.site.register(AdvisorayBoard)
admin.site.register(Article)
admin.site.register(WebAdd)
admin.site.register(WebSiteReview)
admin.site.register(HelpCategory)
admin.site.register(Subscribers)
admin.site.register(Donar)
admin.site.register(BusinessOfferType)
admin.site.register(Bank)
admin.site.register(BusinessOffer)
admin.site.register(BlogType)
admin.site.register(Section)
admin.site.register(RoleName)
admin.site.register(Category)
admin.site.register(Answer)
admin.site.register(ArticleType)
admin.site.register(Status)
admin.site.register(CertificateType)
admin.site.register(ClientMessage)
admin.site.register(ClientReply)
admin.site.register(Collaborations)
admin.site.register(TblClass)
admin.site.register(School)
admin.site.register(Day)
admin.site.register(Department)
admin.site.register(DepartmentBoard)
admin.site.register(Replies)
admin.site.register(Event)
admin.site.register(SuperAdmin)
admin.site.register(Exam)
admin.site.register(TranscationType)
admin.site.register(QuizContext)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(SchoolAssignment)
admin.site.register(Announcement)
admin.site.register(ArticleComments)
admin.site.register(AssignmentResult)
admin.site.register(Blog)
admin.site.register(Client)
admin.site.register(Certificate)
admin.site.register(ClientSchoolComplain)
admin.site.register(ClientCertificate)
admin.site.register(Comments)
admin.site.register(CourseAssignToTeacher)
admin.site.register(Discussion)
admin.site.register(Help)
admin.site.register(KidsStoryType)
admin.site.register(KidsStory)
admin.site.register(KidTalent)
admin.site.register(Lecture)
admin.site.register(Login)
admin.site.register(ManualTest)
admin.site.register(Messages)
admin.site.register(Question)
admin.site.register(OnlineTest)
admin.site.register(OnlineTestAnswers)
admin.site.register(OnlineTestQuestionOption)
admin.site.register(OnlineTestResults)
admin.site.register(Options)
admin.site.register(PaymentConfirmation)
admin.site.register(Post)
admin.site.register(QuizContextResult)
admin.site.register(ResultClient)
admin.site.register(StudentComplain)
admin.site.register(StudentHistory)
admin.site.register(StudentMaster)
admin.site.register(StudentResult)
admin.site.register(SubmitManualTest)
admin.site.register(Team)
admin.site.register(TechnicTip)
admin.site.register(TimeTable)
admin.site.register(UserEnrollInCourse)
admin.site.register(UserFeedBack)
admin.site.register(Attendance)
admin.site.register(Calender)
admin.site.register(Parents)
