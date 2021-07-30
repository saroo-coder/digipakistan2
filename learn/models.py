from django.db import models


# Create your models here.
class AdvisorayBoard(models.Model):#1
    boardid = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    departmentid = models.IntegerField()
    shortdescription = models.TextField(max_length=500)
    longdescription = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name


class WebAdd(models.Model):#2
    addid = models.IntegerField()
    link = models.URLField()
    image = models.ImageField()

    def __str__(self):
        return self.link


class WebSiteReview(models.Model):#3
    reviewid = models.IntegerField()
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=500)
    email = models.EmailField()
    contactno = models.IntegerField()
    createddate = models.DateTimeField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name


class HelpCategory(models.Model):#4
    categoryid = models.IntegerField()
    categoryname = models.CharField(max_length=200)

    def __str__(self):
        return self.categoryname


class Subscribers(models.Model):#5
    subid = models.IntegerField()
    subname = models.CharField(max_length=200, null=True)
    createdon = models.DateTimeField()
    subemail = models.EmailField()

    def __str__(self):
        return self.subname


class Donar(models.Model):#6
    donarid = models.IntegerField()
    categoryid = models.IntegerField()
    name = models.CharField(max_length=200)
    fathername = models.CharField(max_length=200)
    email = models.EmailField()
    nic = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class BusinessOfferType(models.Model):#7
    articletypeid = models.IntegerField()
    articletypename = models.CharField(max_length=200)

    def __str__(self):
        return self.articletypename


class Bank(models.Model):#8
    bankid = models.IntegerField()
    bankname = models.CharField(max_length=200)

    def __str__(self):
        return self.bankname


class BusinessOffer(models.Model):#9
    offerid = models.IntegerField()
    title = models.CharField(max_length=200)
    imgpath = models.ImageField()
    shortdes = models.TextField(max_length=200)
    longdes = models.TextField()
    statusid = models.IntegerField()
    views = models.IntegerField()
    createdate = models.DateTimeField()
    roleid = models.IntegerField()
    articletypeid = models.IntegerField()
    userid = models.IntegerField()
    schoolid = models.IntegerField()

    def __str__(self):
        return self.title


class BlogType(models.Model):#10
    blogtypeid = models.IntegerField()
    blogtypename = models.CharField(max_length=200)

    def __str__(self):
        return self.blogtypename


class Section(models.Model):#11
    sectionid = models.IntegerField()
    sectionname = models.CharField(max_length=500)
    schoolid = models.IntegerField()

    def __str__(self):
        return self.sectionname


class RoleName(models.Model):#12
    roleid = models.IntegerField()
    rolename = models.CharField(max_length=200)

    def __str__(self):
        return self.rolename


class Category(models.Model):#13
    categoryid = models.IntegerField()
    categoryname = models.CharField(max_length=200)

    def __str__(self):
        return self.categoryname


class Answer(models.Model):#14
    answerid = models.IntegerField()
    questionid = models.IntegerField()
    answertext = models.TextField()

    def __str__(self):
        return self.answertext


class ArticleType(models.Model):#15
    articletypeid = models.IntegerField()
    articletypename = models.CharField(max_length=200)

    def __str__(self):
        return self.articletypename


class Status(models.Model):#16
    statusid = models.IntegerField()
    statustype = models.CharField(max_length=200)

    def __str__(self):
        return self.statustype


class CertificateType(models.Model):#17
    certificatetypeid = models.IntegerField()
    certificatetypename = models.CharField(max_length=200)

    def __str__(self):
        return self.certificatetypename


class ClientMessage(models.Model):#18
    messageid = models.IntegerField()
    subject = models.CharField(max_length=1000)
    messagetopost = models.TextField()
    form = models.CharField(max_length=1000)
    dateposted = models.DateTimeField()
    roleid = models.IntegerField()
    userid = models.IntegerField()

    def __str__(self):
        return self.subject


class ClientReply(models.Model):#19
    replyid = models.IntegerField()
    messageid = models.IntegerField()
    replyform = models.CharField(max_length=1000)
    replymessage = models.TextField()
    replydatetime = models.DateTimeField()

    def __str__(self):
        return self.replymessage


class Collaborations(models.Model):#20
    collaborationid = models.IntegerField()
    collaborationname = models.CharField(max_length=200)
    collaborationtitle = models.CharField(max_length=200)
    image = models.ImageField()
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.collaborationname


class TblClass(models.Model):#21
    classid = models.IntegerField()
    name = models.CharField(max_length=200)
    schoolid = models.IntegerField()

    def __str__(self):
        return self.name


class School(models.Model):#22
    schoolid = models.IntegerField()
    schoolname = models.CharField(max_length=200)
    schoolimage = models.ImageField()
    schoolcontactno = models.CharField(max_length=13)
    schooladdress = models.CharField(max_length=500)
    createddate = models.DateTimeField()
    schoolemail = models.EmailField()
    password = models.CharField(max_length=13)

    def __str__(self):
        return self.schoolname


class Day(models.Model):#23
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Department(models.Model):#24
    departmentid = models.IntegerField()
    departmentname = models.CharField(max_length=200)

    def __str__(self):
        return self.departmentname


class DepartmentBoard(models.Model):#25
    departmentid = models.IntegerField()
    departmentname = models.CharField(max_length=200)

    def __str__(self):
        return self.departmentname


class Replies(models.Model):#26
    id = models.IntegerField(primary_key=True)
    messageid = models.IntegerField()
    replyform = models.CharField(max_length=1000)
    replymessage = models.TextField()
    replydate = models.DateTimeField()

    def __str__(self):
        return self.replymessage


class Event(models.Model):#27
    eventid = models.IntegerField()
    title = models.CharField(max_length=200)
    eventstarttime = models.DateTimeField()
    eventendtime = models.DateTimeField()
    eventdescription = models.TextField()
    eventvenue = models.CharField(max_length=200)
    eventvenueimage = models.ImageField()
    eventvenuevideo = models.FileField()

    def __str__(self):
        return self.title


class SuperAdmin(models.Model):#28
    adid = models.IntegerField()
    ademail = models.EmailField()
    adpassword = models.CharField(max_length=13)
    adname = models.CharField(max_length=200)
    adimageurl = models.ImageField()

    def __str__(self):
        return self.adname


class Exam(models.Model):#29
    examid = models.IntegerField()
    examname = models.CharField(max_length=200)

    def __str__(self):
        return self.examname


class TranscationType(models.Model):#30
    transcationtypeid = models.IntegerField()
    transcationtype = models.CharField(max_length=200)

    def __str__(self):
        return self.transcationtype


class QuizContext(models.Model):#31
    questionid = models.IntegerField()
    question = models.CharField(max_length=1000)
    ismultiple = models.BinaryField()
    isactive = models.BinaryField()

    def __str__(self):
        return str(self.isactive)


class Student(models.Model):#32
    id = models.IntegerField(primary_key=True)
    regno = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contactno = models.IntegerField()
    registrationdate = models.DateTimeField()
    address = models.CharField(max_length=200)
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    password = models.CharField(max_length=13)
    imagepath = models.ImageField()
    sectionid = models.IntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):#33
    courseid = models.IntegerField()
    coursedescription = models.TextField()
    coursename = models.CharField(max_length=200)
    userid = models.IntegerField()
    code = models.CharField(max_length=200)
    videolink = models.FileField()
    roleid = models.ForeignKey(RoleName, on_delete=models.CASCADE)
    createddate = models.DateTimeField()
    imagelink = models.ImageField()
    duration = models.DateTimeField()
    longdes = models.TextField()
    coursetype = models.CharField(max_length=200)
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    assignto = models.CharField(max_length=200)
    status = models.BinaryField()

    def __str__(self):
        return self.coursename


class Teacher(models.Model):#34
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    passowrd = models.CharField(max_length=13)
    image = models.ImageField()
    regno = models.CharField(max_length=20)
    joiningdate = models.DateTimeField()

    def __str__(self):
        return self.name


class SchoolAssignment(models.Model):#35
    assignmentid = models.IntegerField()
    assignmentname = models.CharField(max_length=200)
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignmenturl = models.URLField()
    duration = models.DateTimeField()
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    createddate = models.DateTimeField()
    userid = models.IntegerField()

    def __str__(self):
        return self.assignmentname


class Announcement(models.Model):#36
    announcementid = models.IntegerField()
    announcementtitle = models.CharField(max_length=200)
    announcementbody = models.TextField()
    createddate = models.DateTimeField()
    roleid = models.ForeignKey(RoleName, on_delete=models.CASCADE)
    userid = models.IntegerField()
    schoolid = models.IntegerField()

    def __str__(self):
        return self.announcementtitle


class Article(models.Model):#37
    articleid = models.IntegerField()
    title = models.CharField(max_length=200)
    imgpath = models.ImageField()
    shortdes = models.TextField(max_length=200)
    longdes = models.TextField()
    views = models.IntegerField()
    createdate = models.DateTimeField()
    roleid = models.ForeignKey(RoleName, on_delete=models.CASCADE)
    articletypeid = models.ForeignKey(ArticleType, on_delete=models.CASCADE)
    userid = models.IntegerField()
    schoolid = models.IntegerField()

    def __str__(self):
        return self.title


class ArticleComments(models.Model):#38
    commentid = models.IntegerField()
    articleid = models.ForeignKey(Article, on_delete=models.CASCADE)
    commentdescription = models.TextField(max_length=500)
    rating = models.IntegerField()
    commentedon = models.DateTimeField()

    def __str__(self):
        return self.commentdescription


class SubmitAssignment(models.Model):#39
    uploadid = models.IntegerField(primary_key=True)
    submitid = models.IntegerField(null=True)
    assignmentid = models.ForeignKey(SchoolAssignment, on_delete=models.CASCADE)
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    userid = models.IntegerField()
    courseid = models.IntegerField()
    uploadurl = models.URLField()
    createddate = models.DateTimeField()

    def __str__(self):
        return self.uploadurl


class AssignmentResult(models.Model):#40
    assignmentresultid = models.IntegerField(primary_key=True)
    assignmentresult = models.CharField(max_length=500, null=True)
    uploadid = models.ForeignKey(SubmitAssignment, on_delete=models.CASCADE, null=True)
    assignmentid = models.ForeignKey(SchoolAssignment, on_delete=models.CASCADE)
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    userid = models.IntegerField()
    totalmarks = models.IntegerField()
    marksobtained = models.IntegerField()
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    createddate = models.DateTimeField()

    def __str__(self):
        return self.assignmentresult


class Blog(models.Model):#41
    blogid = models.IntegerField()
    blogtypeid = models.ForeignKey(BlogType, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    imgpath = models.ImageField()
    shortdes = models.TextField(max_length=200)
    longdes = models.TextField()
    views = models.IntegerField()
    createdate = models.DateTimeField()
    schoolid = models.IntegerField()

    def __str__(self):
        return self.title


class Client(models.Model):#42
    userid = models.IntegerField()
    username = models.CharField(max_length=200)
    ceratedon = models.DateTimeField()
    email = models.EmailField()
    password = models.CharField(max_length=13)
    certificatetypename = models.CharField(max_length=200)
    cnic = models.IntegerField()
    contactnumber = models.IntegerField()
    image = models.ImageField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    confirmpassword = models.CharField(max_length=13)

    def __str__(self):
        return self.username


class Certificate(models.Model):#43
    certificateid = models.IntegerField()
    certificatetypeid = models.ForeignKey(CertificateType, on_delete=models.CASCADE)
    userid = models.ForeignKey(Client, on_delete=models.CASCADE)
    issuedate = models.DateTimeField()

    def __str__(self):
        return str(self.certificatetypeid)


class ClientSchoolComplain(models.Model):#44
    complainid = models.IntegerField()
    complaindescription = models.TextField()
    complaindate = models.DateTimeField()
    userid = models.IntegerField()
    replymsg = models.TextField()
    roleid = models.ForeignKey(RoleName, on_delete=models.CASCADE)

    def __str__(self):
        return self.complaindescription


class ClientCertificate(models.Model):#45
    certificateid = models.IntegerField()
    certificatetypeid = models.ForeignKey(CertificateType, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    issuedate = models.DateTimeField()
    marksobtained = models.IntegerField()
    percentage = models.FloatField()

    def __str__(self):
        return self.username


class Comments(models.Model):#46
    commentid = models.IntegerField()
    blogid = models.IntegerField()
    body = models.CharField(max_length=500)
    createddate = models.DateTimeField()
    userid = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.body


class CourseAssignToTeacher(models.Model):#47
    assignid = models.IntegerField()
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    teacherid = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.assignid)


class Discussion(models.Model):#48
    threadid = models.IntegerField()
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    classid = models.IntegerField()
    postdate = models.DateTimeField()
    threadtitle = models.CharField(max_length=200)
    schoolid = models.IntegerField()
    userid = models.IntegerField()
    roleid = models.IntegerField()
    sectionid = models.IntegerField()

    def __str__(self):
        return self.threadtitle


class Help(models.Model):#49
    helpid = models.IntegerField()
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    fathername = models.CharField(max_length=200)
    email = models.EmailField()
    nic = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.description


class KidsStoryType(models.Model):#50
    kidsstorytypeid = models.IntegerField()
    kidsstoryname = models.CharField(max_length=500)

    def __str__(self):
        return self.kidsstoryname


class KidsStory(models.Model):#51
    storyid = models.IntegerField()
    storytitle = models.CharField(max_length=500)
    imgpath = models.ImageField()
    shortdes = models.TextField()
    longdes = models.TextField()
    views = models.IntegerField()
    createddate = models.DateTimeField()
    storytypeid = models.ForeignKey(KidsStoryType, on_delete=models.CASCADE)
    schoolid = models.IntegerField()
    statusid = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.storytitle


class KidTalent(models.Model):#52
    talentid = models.IntegerField()
    title = models.CharField(max_length=500)
    videopath = models.FileField()
    shortdes = models.TextField(max_length=200)
    longdes = models.TextField()
    statusid = models.ForeignKey(Status, on_delete=models.CASCADE)
    views = models.IntegerField()
    createddate = models.DateTimeField()
    roleid = models.ForeignKey(RoleName, on_delete=models.CASCADE)
    userid = models.IntegerField()
    schoolid = models.IntegerField()

    def __str__(self):
        return self.title


class Lecture(models.Model):#53
    lectureid = models.IntegerField()
    lecturename = models.CharField(max_length=500)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    lectureurl = models.URLField()
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    createddate = models.DateTimeField()
    videolink = models.URLField()
    lecturedescription = models.TextField()
    userid = models.IntegerField()

    def __str__(self):
        return self.lecturename


class Login(models.Model):#54
    id = models.IntegerField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=13)
    name = models.CharField(max_length=500)
    roleid = models.ForeignKey(RoleName, on_delete=models.CASCADE)
    userid = models.IntegerField()

    def __str__(self):
        return self.name


class ManualTest(models.Model):#55
    testid = models.IntegerField()
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    duration = models.DateTimeField()
    testurl = models.URLField()
    schollid = models.ForeignKey(School, on_delete=models.CASCADE)
    createddate = models.DateTimeField()
    userid = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.testurl


class Messages(models.Model):#56
    id = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=500)
    messagetopost = models.TextField()
    form = models.CharField(max_length=1000)
    dateposted = models.DateTimeField()
    schoolid = models.IntegerField()
    classid = models.IntegerField()
    rollid = models.IntegerField()
    userid = models.IntegerField()
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.messagetopost


class Question(models.Model):#57
    questionid = models.IntegerField()
    question = models.CharField(max_length=10000)
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE)
    ismultiple = models.BinaryField()
    isactive = models.BinaryField()

    def __str__(self):
        return self.question


class OnlineTest(models.Model):#58
    questionid = models.ForeignKey(Question, on_delete=models.CASCADE)
    questionname = models.CharField(max_length=1000)
    ismultiple = models.BinaryField()
    isactive = models.BinaryField()
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    duration = models.DateTimeField()
    roleid = models.ForeignKey(RoleName, on_delete=models.CASCADE)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    createddate = models.DateTimeField()
    userid = models.IntegerField()
    schoolid = models.IntegerField()

    def __str__(self):
        return self.questionname


class OnlineTestAnswers(models.Model):#59
    answerid = models.IntegerField()
    questionid = models.ForeignKey(Question, on_delete=models.CASCADE)
    answertext = models.TextField()
    roleid = models.ForeignKey(RoleName, on_delete=models.CASCADE)
    userid = models.IntegerField()
    schoolid = models.IntegerField()

    def __str__(self):
        return self.answertext


class OnlineTestQuestionOption(models.Model):#60
    optionid = models.IntegerField()
    questionid = models.ForeignKey(Question, on_delete=models.CASCADE)
    optionname = models.CharField(max_length=1000)

    def __str__(self):
        return self.optionname


class OnlineTestResults(models.Model):#61
    onlinetestresults = models.ForeignKey(OnlineTest, on_delete=models.CASCADE)
    questionid = models.IntegerField()
    answertext = models.TextField()
    userid = models.IntegerField()
    roleid = models.ForeignKey(RoleName, on_delete=models.CASCADE)
    schoolid = models.IntegerField()

    def __str__(self):
        return str(self.onlinetestresults)


class Options(models.Model):#62
    optionid = models.IntegerField()
    questionid = models.ForeignKey(Question, on_delete=models.CASCADE)
    optionname = models.CharField(max_length=1000)

    def __str__(self):
        return self.optionname


class PaymentConfirmation(models.Model):#63
    paymentid = models.IntegerField()
    bankid = models.ForeignKey(Bank, on_delete=models.CASCADE)
    accountno = models.IntegerField()
    transactiontypeid = models.ForeignKey(TranscationType, on_delete=models.CASCADE)
    transactionslipnumber = models.CharField(max_length=2000)
    slipurl = models.URLField()
    userid = models.ForeignKey(Client, on_delete=models.CASCADE)
    iban = models.CharField(max_length=2000)

    def __str__(self):
        return self.transactionslipnumber


class Post(models.Model):#64
    postid = models.IntegerField()
    posttitle = models.CharField(max_length=500)
    posttext = models.TextField()
    postdate = models.DateTimeField()
    threadid = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    schoolid = models.IntegerField()
    userid = models.IntegerField()
    roleid = models.ForeignKey(RoleName, on_delete=models.CASCADE)

    def __str__(self):
        return self.posttitle


class QuizContextResult(models.Model):#65
    resultid = models.IntegerField()
    questionid = models.ForeignKey(Question, on_delete=models.CASCADE)
    answertext = models.TextField()
    userid = models.IntegerField()
    createdon = models.DateTimeField()
    status = models.BinaryField()

    def __str__(self):
        return self.answertext


class ResultClient(models.Model):#66
    resultid = models.IntegerField()
    userid = models.ForeignKey(Client, on_delete=models.CASCADE)
    questionid = models.ForeignKey(Question, on_delete=models.CASCADE)
    answertext = models.TextField()

    def __str__(self):
        return self.answertext


class StudentComplain(models.Model):#67
    complainid = models.IntegerField()
    complaindescription = models.TextField()
    complaindate = models.DateTimeField()
    userid = models.ForeignKey(Client, on_delete=models.CASCADE)
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    replymsg = models.TextField()

    def __str__(self):
        return self.complaindescription


class StudentHistory(models.Model):#68
    studenthistoryid = models.IntegerField()
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    lastclass = models.CharField(max_length=200)
    createddate = models.DateTimeField()
    lastclasssection = models.CharField(max_length=200)

    def __str__(self):
        return str(self.studenthistoryid)


class StudentMaster(models.Model):#69
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    examid = models.ForeignKey(Exam, on_delete=models.CASCADE)
    classname = models.CharField(max_length=200)
    regno = models.IntegerField()
    sectionname = models.CharField(max_length=200)
    createdby = models.DateTimeField()

    def __str__(self):
        return self.name


class StudentResult(models.Model):#70
    studentresultid = models.IntegerField()
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    courseid = models.IntegerField()
    totalmarks = models.IntegerField()
    marksobtained = models.IntegerField()
    percentage = models.FloatField()
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    classid = models.IntegerField()
    createddate = models.DateTimeField()
    sectionid = models.ForeignKey(Section, on_delete=models.CASCADE)
    studentmasterid = models.IntegerField()
    examid = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.marksobtained)


class SubmitManualTest(models.Model):#71
    uploadid = models.IntegerField()
    testid = models.ForeignKey(ManualTest, on_delete=models.CASCADE)
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    userid = models.IntegerField()
    courseid = models.IntegerField()
    uploadurl = models.URLField(max_length=150)
    createddate = models.DateTimeField()

    def __str__(self):
        return self.uploadurl


class Team(models.Model):#72
    teamid = models.IntegerField()
    name = models.CharField(max_length=500)
    designationid = models.ForeignKey(Department, on_delete=models.CASCADE)
    shortdescription = models.TextField(max_length=200)
    longdescription = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name


class TechnicTip(models.Model):#73
    tipid = models.IntegerField()
    title = models.CharField(max_length=500)
    videopath = models.FileField()
    shortdes = models.TextField(max_length=200)
    longdes = models.TextField()
    statusid = models.ForeignKey(Status, on_delete=models.CASCADE)
    createddate = models.DateTimeField()
    roleid = models.ForeignKey(RoleName, on_delete=models.CASCADE)
    userid = models.IntegerField()
    schoolid = models.IntegerField()

    def __str__(self):
        return self.title


class TimeTable(models.Model):#74
    id = models.IntegerField(primary_key=True)
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    sectionid = models.ForeignKey(Section, on_delete=models.CASCADE)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    allocationstatus = models.CharField(max_length=500)
    dayid = models.ForeignKey(Day, on_delete=models.CASCADE)
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.starttime)


class UserEnrollInCourse(models.Model):#75
    enrollmentid = models.IntegerField()
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    statusid = models.ForeignKey(Status, on_delete=models.CASCADE)
    enrolldate = models.DateTimeField()
    roleid = models.ForeignKey(RoleName, on_delete=models.CASCADE)
    isuseractive = models.BinaryField()
    userid = models.IntegerField()
    registrationid = models.IntegerField()

    def __str__(self):
        return str(self.isuseractive)


class UserFeedBack(models.Model):#76
    feedbackid = models.IntegerField()
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    createddate = models.DateTimeField()
    userid = models.IntegerField()
    rollid = models.ForeignKey(RoleName, on_delete=models.CASCADE)
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return self.description


class Attendance(models.Model):#77
    attendanceid = models.IntegerField(primary_key=True)
    attendance = models.CharField(max_length=20, null=True)
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacherid = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    daytime = models.DateTimeField()

    def __str__(self):
        return self.attendance


class Calender(models.Model):#78
    # calenderid = models.IntegerField(null=True)
    # calender = models.CharField(max_length=500, null=True)
    date = models.DateTimeField()
    eventid = models.ForeignKey(Event, on_delete=models.CASCADE)
    assignmentid = models.ForeignKey(SchoolAssignment, on_delete=models.CASCADE)
    testid = models.ForeignKey(OnlineTest, on_delete=models.CASCADE)
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.eventid)


class Parents(models.Model):#79
    parentsid = models.IntegerField(primary_key=True)
    studentid = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    studentresultid = models.ForeignKey(StudentResult, on_delete=models.CASCADE)
    assignmentid = models.ForeignKey(SchoolAssignment, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
