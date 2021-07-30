
from client.models import ClientModel
import random
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

# Create your models here.

class SchoolModel(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #admin of school
    title = models.CharField(max_length=50)
    image = models.ImageField(default='default.jpg')
    address = models.CharField(max_length=500)
    email = models.EmailField()
    password = models.CharField(max_length=13)
    contact_no = models.CharField(max_length=12)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TblClassModel(models.Model):
    title = models.CharField(max_length=50)
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True) 
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.title) + '_' + str(r)
        super(TblClassModel, self).save(*args, **kwargs)

class TblSectionModel(models.Model):
    title = models.CharField(max_length=50)
    # school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE, default=0)
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True) 
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.title) + '_' + str(r)
        super(TblSectionModel, self).save(*args, **kwargs)

        
class CourseModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    code = models.CharField(max_length=50)
    video_link = models.FileField(default='default_link')
    image_link = models.URLField(default='default_link')
    long_description = models.TextField()
    course_type = models.CharField(max_length=50)
    classes = models.ForeignKey(TblClassModel, on_delete=models.CASCADE)
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True) 
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.title) + '_' + str(r)
        super(CourseModel, self).save(*args, **kwargs)



class TeacherModel(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    # email = models.EmailField()
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)
    # password_at_time_of_creation = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg')
    # reg_no = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=12)
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True) 
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    designation = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name 

    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.name) + '_' + str(r)
        super(TeacherModel, self).save(*args, **kwargs)

class StudentModel(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_no = models.CharField(max_length=20)
    # email = models.EmailField(max_length=50)
    address = models.CharField(max_length=200)
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE) #in drop down show admin's school 
    # section_id = models.ForeignKey(TblSectionModel, on_delete=models.CASCADE,default=2) #in drop down show admin's school 
    # class_id = models.ForeignKey(TblClassModel, on_delete=models.CASCADE,default=2) #in drop down show admin's school 
    password_at_time_of_creation = models.CharField(max_length=100)
    imagepath = models.ImageField(max_length=100, default='default.jpg')
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True) 
    section_id = models.CharField(max_length=12)
    class_id = models.CharField(max_length=12)
    contact_no = models.CharField(max_length=12)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.name) + '_' + str(r)
        super(StudentModel, self).save(*args, **kwargs)

class Assign_TeacherModel(models.Model):
    teacher = models.ForeignKey(TeacherModel,on_delete=models.CASCADE , related_name='assignteachers')
    classes = models.ForeignKey(TblClassModel , on_delete=models.CASCADE , related_name='assignclasses')
    course = models.ForeignKey(CourseModel , on_delete= models.CASCADE , related_name='assigncourses')

    def __str__(self):
        return '%d: %s' % (self.id, self.teacher.name)

class Enroll_StudentModel(models.Model):
    student = models.ForeignKey(StudentModel,on_delete=models.CASCADE )
    classes = models.ForeignKey(TblClassModel , on_delete=models.CASCADE , related_name='enrollStudents')
    course = models.ForeignKey(CourseModel , on_delete= models.CASCADE )

    def __str__(self):
        return '%s: %s' % (self.course.title, self.student.name)

class ContactFormModel(models.Model):
    student = models.ForeignKey(StudentModel,on_delete=models.CASCADE )
    query = models.TextField()
    response = models.TextField(default='None')
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    response_submitted = models.BooleanField(default=False)



class AnnouncementModel(models.Model):

    title = models.CharField(max_length=50)
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
        return reverse('event_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)



class RoomModel(models.Model):
    title = models.CharField(max_length=50)
    student = models.ForeignKey(StudentModel,on_delete=models.CASCADE )
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


class ParentModel(models.Model):
    parent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE) #in drop down show admin's school 
    password_at_time_of_creation = models.CharField(max_length=100)
    imagepath = models.ImageField(max_length=100, default='default.jpg')
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True) 
    contact_no = models.CharField(max_length=12)
    created_at = models.DateTimeField (auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.name) + '_' + str(r)
        super(ParentModel, self).save(*args, **kwargs)

class Enroll_ParentModel(models.Model):
    parent = models.ForeignKey(ParentModel,on_delete=models.CASCADE )
    student = models.ForeignKey(StudentModel,on_delete=models.CASCADE )
    classes = models.ForeignKey(TblClassModel , on_delete=models.CASCADE , related_name='enrollParent')
    course = models.ForeignKey(CourseModel , on_delete= models.CASCADE )

    
    def __str__(self):
        return self.parent.name
