from django.db import models
from django.test import client
from auth_users.models import User
from django.conf import settings
from django.template.defaultfilters import slugify
from adminapp.models import *
from django.contrib.auth.models import AbstractUser
import random
from django.utils.timezone import now
from datetime import date
from client.models import ClientModel

# Create your models here.


class DiscussionModel(models.Model): #Q

    #type = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    #image = models.ImageField(upload_to ="complaint/", blank=False, null=False,default="/image.jpg/")
    slug = models.SlugField(max_length=250,null=True, unique=True)
    short_description = models.CharField(max_length=700)
    long_description = models.CharField(max_length=1400)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('article_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

class ScheduleModel(models.Model): #(move into admin)

    type = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,null=True, unique=True)
    image = models.ImageField(upload_to ="article/", blank=False, null=False,default="/image.jpg/")
    short_description = models.CharField(max_length=700)
    long_description = models.CharField(max_length=1400)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('article_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)



class ArticleModel(models.Model):

    ARTICLE_STATUS = (
        ('D', 'Draft'),
        ('P', 'Published'),
    )
    status = models.CharField(
        max_length=1,
        choices=ARTICLE_STATUS,
        default='D',
        help_text='Status of blogs',
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to ="blog/")
    short_description = models.CharField(max_length=700)
    long_description = models.CharField(max_length=1400)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250,null=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

class BlogModel(models.Model):

    BLOG_STATUS = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    status = models.CharField(
        max_length=1,
        choices=BLOG_STATUS,
        default='d',
        help_text='Status of blogs',
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to ="blog/")
    short_description = models.CharField(max_length=700)
    long_description = models.CharField(max_length=1400)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250,null=True, unique=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('blog_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class EventModel(models.Model):
    date = models.DateField("Day of Event")
    title = models.CharField(max_length=50)
    event_start_time = models.TimeField("Starting Time")
    event_end_time = models.TimeField("Ending Time")
    short_description = models.CharField(max_length=700)
    long_description = models.CharField(max_length=1400)
    venue = models.CharField(max_length=200)
    venue_image = models.ImageField(help_text="Add picture related to event")
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('event_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)




# class SchoolModel(models.Model):
#     title = models.CharField(max_length=50)
#     name = models.CharField(max_length=50)
#     slug = models.SlugField(max_length=250,null=True, unique=True)
#     contact = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     password = models.CharField(max_length=700)
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         kwargs = {
#             'slug': self.slug
#         }
#         return reverse('article_detail', kwargs=kwargs)
#     def save(self, *args, **kwargs):
#         value = self.title
#         self.slug = slugify(value,)
#         super().save(*args, **kwargs)

# class SubjectModel(models.Model):
#     title = models.CharField(max_length=50,default="anything")
#     slug = models.SlugField(max_length=250,null=True, unique=True)
#     #teacher = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
#     #class_standard = models.ForeignKey(ClassStandardModel,on_delete=models.CASCADE,default=1)
#     short_discription = models.CharField(max_length=700)
#     long_discription = models.CharField(max_length=1400)
#     created_at = models.DateTimeField (auto_now=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.title
#     def get_absolute_url(self):
#         kwargs = {
#             'slug': self.slug
#         }
#
#         return reverse('subject_detail', kwargs=kwargs)
#     def save(self, *args, **kwargs):
#         value = self.title
#         self.slug = slugify(value,)
#         super().save(*args, **kwargs)
class BusinessPartnersModel(models.Model): #BusinesPartners
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,null=True, unique=True)
    image = models.ImageField(upload_to ="callobration/", blank=False, null=True)
    #user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    short_description = models.CharField(max_length=700)
    long_description = models.CharField(max_length=1400)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

# class CourseModel(models.Model):
    
#     title = models.CharField(max_length=700) 
#     category = models.CharField(max_length=50)
#     slug = models.SlugField(max_length=250,null=True, unique=True)
#     short_description = models.CharField(max_length=700)
#     long_description = models.CharField(max_length=1400)
#     image = models.ImageField(upload_to ="course/", blank=False, null=True)
#     video_link = models.FileField(default='default_link')
#     created_at = models.DateTimeField (auto_now=True)
#     updated_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         kwargs = {
#             'slug': self.slug
#         }
#         return reverse('course_detail', kwargs=kwargs)
#     def save(self, *args, **kwargs):
#         value = self.title
#         self.slug = slugify(value,)
#         super().save(*args, **kwargs)


# class Enroll_CourseModel(models.Model):
#     client = models.ForeignKey(ClientModel , on_delete=models.CASCADE)
#     course = models.ForeignKey(CourseModel,on_delete=models.CASCADE )
    

#     def __str__(self):
#         return '%s: %s' % (self.course.title, self.client.name)

# class QuestionModel(models.Model):
#     title = models.CharField(max_length=700)
#     course_id = models.ForeignKey(CourseModel,related_name="Questions",on_delete=models.CASCADE,max_length=700)
#     option1 = models.CharField(max_length=700)
#     option2 = models.CharField(max_length=700)
#     option2 = models.CharField(max_length=700)
#     option4 = models.CharField(max_length=700)
#     slug = models.SlugField(max_length=250,null=True, unique=True)
#     created_at = models.DateTimeField (auto_now=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.questions
#     def get_absolute_url(self):
#         kwargs = {
#             'slug': self.slug
#         }
#         return reverse('article_detail', kwargs=kwargs)
#     def save(self, *args, **kwargs):
#         value = self.title
#         self.slug = slugify(value,)
#         super().save(*args, **kwargs)



# class TestModel(models.Model):

#     title = models.CharField(max_length=50)
#     slug = models.SlugField(max_length=250,null=True, unique=True)
#     test= models.FileField(max_length=100, default='no video', upload_to='media')
#     short_description = models.CharField(max_length=700)
#     long_description = models.CharField(max_length=1400)
#     created_at = models.DateTimeField (auto_now=True)
#     updated_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
#     def get_absolute_url(self):
#         kwargs = {
#             'slug': self.slug
#         }
#         return reverse('event_detail', kwargs=kwargs)
#     def save(self, *args, **kwargs):
#         value = self.title
#         self.slug = slugify(value,)
#         super().save(*args, **kwargs)

class ClientCourseModel(models.Model):
    course = models.CharField(max_length=700) 
    category = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,null=True, unique=True,blank=True)
    short_description = models.CharField(max_length=700)
    long_description = models.CharField(max_length=1400)
    image = models.ImageField(upload_to ="course/", blank=True, null=True)
    video_link = models.FileField(default='default_link',null=True)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.course

    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.course) + '-' + str(r)
        super(ClientCourseModel, self).save(*args, **kwargs)

class Enroll_CourseModel(models.Model):
    title = models.CharField(max_length=700)
    client = models.ForeignKey(ClientModel , on_delete=models.CASCADE)
    course = models.ForeignKey(ClientCourseModel,on_delete=models.CASCADE )
    

    def __str__(self):
        return f"{self.course.course}-{self.client.name}"


class QuestionModel(models.Model):
    title = models.CharField(max_length=700)
    course_id = models.ForeignKey(ClientCourseModel,related_name="Questions",on_delete=models.CASCADE,max_length=700)
    question = models.CharField(max_length = 500)
    option1 = models.CharField(max_length = 20)
    option2 = models.CharField(max_length = 20)
    option3 = models.CharField(max_length = 20)
    option4 = models.CharField(max_length = 20)
    answer = models.CharField(max_length = 20)
    slug = models.SlugField(max_length=250,null=True, unique=True)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.questions
    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('article_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

class Client_SubmitquestionModel(models.Model):
    question = models.ForeignKey(QuestionModel,related_name="Question",on_delete=models.CASCADE)
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    course = models.ForeignKey(ClientCourseModel, on_delete=models.CASCADE)
    submitted_file = models.FileField(max_length=100, default='no file',upload_to='media')
    is_submit = models.BooleanField(default=False)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class AnnouncementModel(models.Model):

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,null=True, unique=True)
    short_description = models.CharField(max_length=700)
    long_description = models.CharField(max_length=1400)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

class Client_testModel(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey(ClientCourseModel,on_delete=models.CASCADE)
    test = models.FileField(max_length=100, default='no test yet',upload_to='media')
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.title) + '-' + str(r)
        super(Client_testModel, self).save(*args, **kwargs) 


class Client_SubmittestModel(models.Model):
    test = models.ForeignKey(Client_testModel, related_name='submitTest',on_delete=models.CASCADE)
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    course = models.ForeignKey(ClientCourseModel, on_delete=models.CASCADE)
    submitted_file = models.FileField(max_length=100, default='no file',upload_to='media')
    is_submit = models.BooleanField(default=False)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)        

class KidStoryModel(models.Model):

    STORY_STATUS = (
        ('D', 'Draft'),
        ('P', 'Published'),
    )

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,null=True, unique=True)
    image = models.ImageField(upload_to ="KidsStory/")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    short_description = models.CharField(max_length=700)
    long_description = models.CharField(max_length=1400)
    status = models.CharField(
        max_length=1,
        choices=STORY_STATUS,
        default='D',
        help_text='Status of kids story',
    )
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class KidTalentModel(models.Model):

    TALENT_STATUS = (
        ('D', 'Draft'),
        ('P', 'Published'),
    )

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,null=True, unique=True)
    image = models.ImageField(upload_to ="kidsTalent/")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    short_description = models.CharField(max_length=700)
    long_description = models.CharField(max_length=1400)
    status = models.CharField(
        max_length=1,
        choices=TALENT_STATUS,
        default='D',
        help_text='Status of kids talent',
    )
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

class QuizContextModel(models.Model):

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,null=True, unique=True)
    #course = models.ForeignKey(CourseModel,null=False,blank=False, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=700)
    long_description = models.CharField(max_length=1400)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('blog_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)



class BusinessPromotionModel(models.Model): #BusinessPromotionModel

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,null=True, unique=True)
    image = models.ImageField(upload_to ="BusinessOffer/", blank=False, null=True)
    #user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    short_description = models.CharField(max_length=700)
    long_description = models.CharField(max_length=1400)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('blog_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)



class TeamModel(models.Model):

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,null=True, unique=True)
    image = models.ImageField(upload_to ="blog/", blank=False, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True)
    short_description = models.CharField(max_length=700)
    long_description = models.CharField(max_length=1400)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('event_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

class AdvisoryBoardModel(models.Model):

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,null=True, unique=True)
    designation = models.CharField(max_length=50)
    short_description = models.CharField(max_length=700)
    long_description = models.CharField(max_length=1400)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('event_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class ClientFeedBackModel(models.Model):
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name= 'courses')
    description = models.CharField(max_length=500)
    client = models.ForeignKey(ClientModel,on_delete=models.CASCADE , related_name='students')
    option = [('Good','Good'),('Average','Average'),('Bad','Bad')]
    rating = models.CharField(max_length=100, choices=option, default='none')
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s: %s' % (self.course.title, self.client.title)
    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class ClientComplainModel(models.Model):
    title = models.CharField(max_length=50)
    client = models.ForeignKey(ClientModel,on_delete=models.CASCADE )
    complain = models.TextField()
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class SubmitClientComplainModel(models.Model):
    complain_id = models.ForeignKey(ClientComplainModel, related_name='ClientComplainModel',on_delete=models.CASCADE)
    is_submit = models.BooleanField(default=False)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class WebsiteAdModel(models.Model):

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,null=True, unique=True)
    image = models.ImageField(upload_to ="blog/", blank=False, null=True)
    #user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    short_description = models.CharField(max_length=700)
    long_description = models.CharField(max_length=1400)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('event_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class JobClassifiedModel(models.Model):

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,null=True, unique=True)
    image = models.ImageField(upload_to ="job/", blank=False, null=True)
    short_description = models.CharField(max_length=700)
    long_description = models.CharField(max_length=1400)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('job_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class CustomerReviewModel(models.Model):

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,null=True, unique=True)
    long_description = models.CharField(max_length=1400)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)
