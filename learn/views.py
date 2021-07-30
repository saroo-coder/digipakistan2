from django.http import request
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import reverse
from .models import *


# Create your views here.

def dashboard(request):
    # dashboard = Dashboard.objects.all()
    return render(request, 'learn/dashboard.html')  # , {'dashboard': dashboard})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginuser')
    else:
        form = UserCreationForm()
    return render(request, 'learn/register.html', {'form': form})


def loginuser(request):
    loginuser = get_object_or_404('klass')
    return render(request, 'learn/loginuser.html', {'loginuser': loginuser})


def index(response):
    template = loader.get_template('learn/base.html')  # getting our template
    return render(request, template.render())


def articles(request):
    articles = Article.objects.all()
    return render(request, 'learn/articles.html', {'articles': articles})


def advisorayboard(request):
    advisorayboard = AdvisorayBoard.objects.all()
    return render(request, 'learn/advisorayboard.html', {'advisorayboard': advisorayboard})


def webadd(request):
    webadd = WebAdd.objects.all()
    return render(request, 'learn/webadd.html', {'webadd': webadd})


def websitereview(request):
    websitereview = WebSiteReview.objects.all()
    return render(request, 'learn/websitereview.html', {'websitereview': websitereview})


def helpcategory(request):
    helpcategory = HelpCategory.objects.all()
    return render(request, 'learn/helpcategory.html', {'helpcategory': helpcategory})


def subscribers(request):
    subscribers = Subscribers.objects.all()
    return render(request, 'learn/subscribers.html', {'subscribers': subscribers})


def donar(request):
    donar = Donar.objects.all()
    return render(request, 'learn/donar.html', {'donar': donar})


def businessoffertype(request):
    businessoffertype = BusinessOfferType.objects.all()
    return render(request, 'learn/businessoffertype', {'businessoffertype': businessoffertype})


def bank(request):
    bank = Bank.objects.all()
    return render(request, 'learn/bank.html', {'bank': bank})


def businessoffer(request):
    businessoffer = BusinessOffer.objects.all()
    return render(request, 'learn/businessoffer', {'businessoffer': businessoffer})


def blogtype(request):
    blogtype = BlogType.objects.all()
    return render(request, 'learn/blogtype.html', {'blogtype': blogtype})


def section(request):
    section = Section.objects.all()
    return render(request, 'learn/section.html', {'section': section})


def rolename(request):
    rolename = RoleName.objects.all()
    return render(request, 'learn/rolename.html', {'rolename': rolename})


def category(request):
    category = Category.objects.all()
    return render(request, 'learn/category.html', {'category': category})


def answer(request):
    answer = Answer.objects.all()
    return render(request, 'learn/answer.html', {'answer': answer})


def articletype(request):
    articletype = ArticleType.objects.all()
    return render(request, 'learn/articletype.html', {'articletype': articletype})


def status(request):
    status = Status.objects.all()
    return render(request, 'learn/status.html', {'status': status})


def certificatetype(request):
    certificatetype = CertificateType.objects.all()
    return render(request, 'learn/certificatetype.html', {'ceritficatetype': certificatetype})


def clientmessage(request):
    clientmessage = ClientMessage.objects.all()
    return render(request, 'learn/clientmessage.html', {'clientmessage': clientmessage})


def clientreply(request):
    clientreply = ClientReply.objects.all()
    return render(request, 'learn/clientreply.html', {'clientreply': clientreply})


def collaborations(request):
    collaborations = Collaborations.objects.all()
    return render(request, 'link/collaborations.html', {'collabortaions': collaborations})


def tblclass(request):
    tblclass = TblClass.objects.all()
    return render(request, 'learn/tblclass.html', {'tblclass': tblclass})


def school(request):
    school = School.objects.all()
    return render(request, 'learn/school.html', {'school': school})


def day(request):
    day = Day.objects.all()
    return render(request, 'learn/day.html', {'day': day})


def department(request):
    department = Department.objects.all()
    return render(request, 'learn/department.html', {'department': department})


def departmentboard(request):
    departmentboard = DepartmentBoard.objects.all()
    return render(request, 'learn/departmentboard', {'departmentboard': departmentboard})


def replies(request):
    replies = Replies.objects.all()
    return render(request, 'learn/replies.html', {'replies': replies})


def event(request):
    event = Event.objects.all()
    return render(request, 'learn/event.html', {'event': event})


def superadmin(request):
    superadmin = SuperAdmin.objects.all()
    return render(request, 'learn/superadmin.html', {'superadmin': superadmin})


def exam(request):
    exam = Exam.objects.all()
    return render(request, 'learn/exam.html', {'exam': exam})


def transcationtypes(request):
    transcationtypes = TranscationType.objects.all()
    return render(request, 'learn/transcationtype.html', {'transcationtypes': transcationtypes})


def quizcontext(request):
    quizcontext = QuizContext.objects.all()
    return render(request, 'learn/quizcontext.html', {'quizcontext': quizcontext})


def student(request):
    student = Student.objects.all()
    return render(request, 'learn/student.html', {'student': student})


def course(request):
    course = Course.objects.all()
    return render(request, 'learn/course.html', {'course': course})


def teacher(request):
    teacher = Teacher.objects.all()
    return render(request, 'learn/teacher.html', {'teacher': teacher})


def schoolassignment(request):
    schoolassignment = SchoolAssignment.objects.all()
    return render(request, 'learn/schoolassignment.html', {'schoolassignment': schoolassignment})


def announcement(request):
    announcement = Announcement.objects.all()
    return render(request, 'learn/announcement.html', {'announcement': announcement})


def articlecomments(request):
    articlecomments = ArticleComments.objects.all()
    return render(request, 'learn/articlescomments.html', {'articlecomments': articlecomments})


def submitassignment(request):
    submitassignment = SubmitAssignment.objects.all()
    return render(request, 'learn/submitassignment.html', {'submitassignment': submitassignment})


def assignmentresult(request):
    assignmentresult = AssignmentResult.objects.all()
    return render(request, 'learn/assignmentresult.html', {'assignmentresult': assignmentresult})


def blog(request):
    blog = Blog.objects.all()
    return render(request, 'learn/blog.html', {'blog': blog})


def client(request):
    client = Client.objects.all()
    return render(request, 'learn/client.html', {'client': client})


def certificate(request):
    certificate = Certificate.objects.all()
    return render(request, 'learn/certificate.html', {'certificate': certificate})


def clientschoolcomplain(request):
    clientschoolcomplain = ClientSchoolComplain.objects.all()
    return render(request, 'learn/clientschoolcomplain.html', {'clientschoolcomplain': clientschoolcomplain})


def clientcertificate(request):
    clientcertificate = ClientCertificate.objects.all()
    return render(request, 'learn/clientcertificate.html', {'clientcertificate': clientcertificate})


def comments(request):
    comments = Comments.objects.all()
    return render(request, 'learn/comments.html', {'comments': comments})


def courseassigntoteacher(request):
    courseassigntoteacher = CourseAssignToTeacher.objects.all()
    return render(request, 'learn/courseassigntoteacher.html', {'courseassigntoteacher': courseassigntoteacher})


def discussion(request):
    discussion = Discussion.objects.all()
    return render(request, 'learn/discussion.html', {'discussion': discussion})


def helps(request):
    helps = Help.objects.all()
    return render(request, 'learn/help.html', {'helps': helps})


def kidsstorytype(request):
    kidsstorytype = KidsStoryType.objects.all()
    return render(request, 'learn/kidsstorytype.html', {'kidsstorytype': kidsstorytype})


def kidsstory(request):
    kidsstory = KidsStory.objects.all()
    return render(request, 'learn/kidsstory.html', {'kidsstory': kidsstory})


def kidtalent(request):
    kidtalent = KidTalent.objects.all()
    return render(request, 'learn/kidtalent.html', {'kidtalent': kidtalent})


def lecture(request):
    lecture = Lecture.objects.all()
    return render(request, 'learn/lecture.html', {'lecture': lecture})


def login(request):
    login = Login.objects.all()
    return render(request, 'learn/login.html', {'login': login})


def manualtest(request):
    manualtest = ManualTest.objects.all()
    return render(request, 'learn/manaualtest.html', {'manualtest': manualtest})


def messages(request):
    messages = Messages.objects.all()
    return render(request, 'learn/message.html', {'messages': messages})


def questions(request):
    questions = Question.objects.all()
    return render(request, 'learn/questions.html', {'questions': questions})


def onlinetest(request):
    onlinetest = OnlineTest.objects.all()
    return render(request, 'learn/onlinetest', {'onlinetest': onlinetest})


def onlinetestanswers(request):
    onlinetestanswers = OnlineTestAnswers.objects.all()
    return render(request, 'learn/onlinetestanswers.html', {'onlinetestanswers': onlinetestanswers})


def onlinetestquestionoption(request):
    onlinetestquestionoption = OnlineTestQuestionOption.objects.all()
    return render(request, 'learn/onlinetestquestionoption.html',
                  {'onlinetestquestionoption': onlinetestquestionoption})


def onlinetestresult(request):
    onlinetestresult = OnlineTestResults.objects.all()
    return render(request, 'learn/onlinetestresult.html', {'onlinetestresult': onlinetestresult})


def options(request):
    options = Options.objects.all()
    return render(request, 'learn/option.html', {'options': options})


def paymentconfirmation(request):
    paymentconfirmation = PaymentConfirmation.objects.all()
    return render(request, 'learn/paymentconfirmation.html', {'paymentconfirmation': paymentconfirmation})


def post(request):
    post = Post.objects.all()
    return render(request, 'learn/post.html', {'post': post})


def quizcontextresult(request):
    quizcontextresult = QuizContextResult.objects.all()
    return render(request, 'learn/quizcontextresult.html', {'quizcontextresult': quizcontextresult})


def resultclient(request):
    resultclient = ResultClient.objects.all()
    return render(request, 'learn/resultclient.html', {'resultclient': resultclient})


def studentcomplain(request):
    studentcomplain = StudentComplain.objects.all()
    return render(request, 'learn/studentcomplain.html', {'studentcomplain': studentcomplain})


def studenthistory(request):
    studenthistory = StudentHistory.objects.all()
    return render(request, 'learn/studenthistory.html', {'studenthistory': studenthistory})


def studentmaster(request):
    studentmaster = StudentMaster.objects.all()
    return render(request, 'learn/studentmaster.html', {'studentmaster': studentmaster})


def studentresult(request):
    studentresult = StudentResult.objects.all()
    return render(request, 'learn/studentresult.html', {'studentresult': studentresult})


def submitmanualtest(request):
    submitmanualtest = SubmitManualTest.objects.all()
    return render(request, 'learn/submitmanualtest.html', {'submitmanualtest': submitmanualtest})


def team(request):
    team = Team.objects.all()
    return render(request, 'learn/team.html', {'team': team})


def technictip(request):
    technictip = TechnicTip.objects.all()
    return render(request, 'learn/technictip.html', {'technictip': technictip})


def timetable(request):
    timetable = TimeTable.objects.all()
    return render(request, 'learn/timetable.html', {'timetable': timetable})


def userenrollincourse(request):
    userenrollincourse = UserEnrollInCourse.objects.all()
    return render(request, 'learn/userenrollincourse.html', {'userenrollincourse': userenrollincourse})


def userfeedback(request):
    userfeedback = UserFeedBack.objects.all()
    return render(request, 'learn/userfeedback.html', {'userfeedback': userfeedback})


def attendances(request):
    attendances = Attendance.objects.all()
    return render(request, 'learn/attendances.html', {'attendances': attendances})


def calender(request):
    calender = Calender.objects.all()
    return render(request, 'learn/calender.html', {'calender': calender})


def parents(request):
    parents = Parents.objects.all()
    return render(request, 'learn/parents.html', {'parents': parents})
