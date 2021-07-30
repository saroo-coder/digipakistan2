from django.db import models
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
import random
from adminapp.models import *
# from superadmin.models import CourseModel,OnlineTestModel, QuestionModel,ContentModel,AnnouncementModel, TestModel, NotesModel
# Create your models here.

class RoleNameModel(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class LectureModel(models.Model):
    title = models.CharField(max_length=150)
    tutorial_link = models.CharField(max_length=100)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    Class = models.ForeignKey(TblClassModel, on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE)
    # school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)
    notes = models.FileField(max_length=100, upload_to='media')
    recorded_lecture= models.FileField(max_length=100, upload_to='media')
    description = models.TextField(max_length=500)
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.title) + '-' + str(r)
        super(LectureModel, self).save(*args, **kwargs)


class AssignmentModel(models.Model):
    title = models.CharField(max_length=50)
    Class = models.ForeignKey(TblClassModel, related_name='classname' ,on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, related_name='coursename', on_delete=models.CASCADE)
    assignment = models.FileField(max_length=100 ,upload_to='media')
    #school = models.ForeignKey(SchoolModel, related_name='school', on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherModel, related_name='teachername', on_delete=models.CASCADE, default= 0)
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True)
    due_at = models.DateTimeField()
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.title) + '-' + str(r)
        super(AssignmentModel, self).save(*args, **kwargs)


class_attendance = (
    ('Present','Present'),
    ('Absent','Absent'),
    ('Null','Null')
)        
class StudentAttendanceModel(models.Model):
    title = models.CharField(max_length=50)
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    Class = models.ForeignKey(TblClassModel, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True)
    short_description = models.CharField(max_length=700)
    mark_attendance = models.CharField(max_length=50, choices=class_attendance)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.title) + '-' + str(r)
        super(StudentAttendanceModel, self).save(*args, **kwargs)
        
class TeacherAnnouncementModel(models.Model):
    title = models.CharField(max_length=50)
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    Class = models.ForeignKey(TblClassModel, on_delete=models.CASCADE)
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True)
    short_description = models.CharField(max_length=700)
    long_description = models.CharField(max_length=1000)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.title) + '-' + str(r)
        super(TeacherAnnouncementModel, self).save(*args, **kwargs)

class testModel(models.Model):
    title = models.CharField(max_length=50)
    classes = models.ForeignKey(TblClassModel,on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel,on_delete=models.CASCADE)
    test = models.FileField(max_length=100, default='no test yet',upload_to='media')
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True)
    due_at = models.DateTimeField()
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.title) + '-' + str(r)
        super(testModel, self).save(*args, **kwargs)

class createQuizModel(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    classes = models.ForeignKey(TblClassModel, on_delete=models.CASCADE)
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return (self.title)

    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.title) + '-' + str(r)
        super(createQuizModel, self).save(*args, **kwargs)

class quizQuestionsAndAnswersModel(models.Model):
    title=models.CharField(max_length=20 , default=0)
    quiz=models.ForeignKey(createQuizModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    question = models.CharField(max_length = 500)
    option1 = models.CharField(max_length = 20)
    option2 = models.CharField(max_length = 20)
    option3 = models.CharField(max_length = 20)
    option4 = models.CharField(max_length = 20)
    answer = models.CharField(max_length = 20)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True)

    def __str__ (self):
        return (self.title)

    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.title) + '-' + str(r)
        super(quizQuestionsAndAnswersModel, self).save(*args, **kwargs)


class SubmittestModel(models.Model):
    test = models.ForeignKey(testModel, related_name='submitTest',on_delete=models.CASCADE)
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    submitted_file = models.FileField(max_length=100, default='no file',upload_to='media')
    is_submit = models.BooleanField(default=False)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class SubmitquestionModel(models.Model):
    question = models.ForeignKey(quizQuestionsAndAnswersModel, related_name='quizQuestionsAndAnswers',on_delete=models.CASCADE)
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    submitted_file = models.FileField(max_length=100, default='no file',upload_to='media')
    is_submit = models.BooleanField(default=False)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class SubmitAssignmentModel(models.Model):
    assignment = models.ForeignKey(AssignmentModel, related_name='submitAssignment',on_delete=models.CASCADE)
    # school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    # course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    submitted_file = models.FileField(max_length=100, default='no file',upload_to='media')
    is_submit = models.BooleanField(default=False)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class StudentFeedBackModel(models.Model):
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    Class = models.ForeignKey(TblClassModel, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    # teacher = models.ManyToManyField(TeacherModel)
    student = models.ForeignKey(StudentModel,on_delete=models.CASCADE)
    option = [('Good','Good'),('Average','Average'),('Bad','Bad')]
    rating = models.CharField(max_length=100, choices=option, default='none')
    created_at = models.DateTimeField (auto_now=True)

class ParentFeedBackModel(models.Model):
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    Class = models.ForeignKey(TblClassModel, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    # teacher = models.ManyToManyField(TeacherModel)
    parent = models.ForeignKey(ParentModel,on_delete=models.CASCADE)
    option = [('Good','Good'),('Average','Average'),('Bad','Bad')]
    rating = models.CharField(max_length=100, choices=option, default='none')
    created_at = models.DateTimeField (auto_now=True)


class DiscussionModel(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    Class = models.ForeignKey(TblClassModel, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return "{}".format(self.course)

    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.course) + '-' + str(r)
        super(DiscussionModel, self).save(*args, **kwargs)

class DiscussionAnswer(models.Model):
    discussion = models.ForeignKey(DiscussionModel,related_name='answers', on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE, null=True, blank=True)
    reply = models.TextField(null=False)


class CalenderModel(models.Model):
    title = models.CharField(max_length=200 )
    details = models.CharField(max_length=200 , default='NULL')
    due_date = models.DateField()
    classes = models.ForeignKey(TblClassModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True)

    def __str__ (self):
        return (self.title)

    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.title) + '-' + str(r)
        super(CalenderModel, self).save(*args, **kwargs)


class ResultModel(models.Model):
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    Class = models.ForeignKey(TblClassModel, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    total_marks = models.CharField(max_length= 10 )
    obtained_marks = models.CharField(max_length= 10 )
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.student.username

class NotesModel(models.Model):
    title = models.CharField(max_length=50)
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE, default= 0)
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True)
    due_at = models.DateTimeField()
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.title) + '-' + str(r)
        super(NotesModel, self).save(*args, **kwargs)
