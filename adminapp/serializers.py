from rest_framework import serializers
from adminapp.models import *
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.contrib.auth import get_user_model, authenticate
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.contrib.auth import get_user_model

User = get_user_model()

def get_user_from_token(request): 
    '''It will given the current username by using token'''
    token = request.user.auth_token
    user = User.objects.get(id=token.user_id)
    return user

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolModel
        fields = '__all__'
        # fields = ['id' , 'title']


class TblClassSerializer(serializers.ModelSerializer):
    enrollStudents = serializers.StringRelatedField(many=True)
    class Meta:
        model = TblClassModel
        fields = '__all__'
        # fields = ['id' , 'title' , 'school','enrollStudents']

class TblSectionSerializer(serializers.ModelSerializer):
    # enrollStudents = serializers.StringRelatedField(many=True)
    class Meta:
        model = TblSectionModel
        fields = '__all__'
        # fields = ['id' , 'title' , 'school','enrollStudents']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = '__all__'

class ViewTeacherSerializer(serializers.ModelSerializer):
    # assignteacher = serializers.StringRelatedField(many=True)
    class Meta:
        model = TeacherModel
        fields = '__all__'

        # fields = ['id' ,'slug', 'title','address' , 'email' , 'image', 'reg_no' ,'created_at', 'updated_at']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementModel
        fields = '__all__'

class ViewCourseSerializer(serializers.ModelSerializer):
    # assigncourses = serializers.StringRelatedField(many=True)
    class Meta:
        model = CourseModel
        fields = '__all__'
        # fields = ['id' , 'title','description' , 'code', 'course_type' , 'classes.title' ,'section.title','created_at']

class ViewAssignCourseSerializer(serializers.ModelSerializer):
    classes = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()
    class Meta:
        model = Assign_TeacherModel
        fields = '__all__'

    def get_course(self,obj):
        return {
            "course_id": obj.course.id,
            "course": obj.course.title,
            }
    
    def get_classes(self,obj):
        return {
            "class_id": obj.classes.id,
            "class": obj.classes.title,
            }

class AssignCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assign_TeacherModel
        fields = '__all__'



class ViewEnrollStudentSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(read_only = True)
    classes = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()

    class Meta:
        model = Enroll_StudentModel
        fields = '__all__'

class EnrollStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroll_StudentModel
        fields = '__all__'

class ViewQuerySerializer(serializers.ModelSerializer):   #Student-Complain
    class Meta:
        model = ContactFormModel
        fields = ['id','student','query','created_at']

class ResponseSerializer(serializers.ModelSerializer):
    response = serializers.CharField(required=True)
    class Meta:
        model = ContactFormModel
        fields = ['response','updated_at','response_submitted']


class StudentRegisterationSerializer(serializers.ModelSerializer,RegisterSerializer):
    student = serializers.PrimaryKeyRelatedField(read_only=True,)

    class Meta:
        model = StudentModel
        fields = '__all__'

    def get_cleaned_data(self): #customization of rest_auth library code
            data = super(StudentRegisterationSerializer, self).get_cleaned_data()
            extra_data = {
                'name': self.validated_data.get('name', ''),
                'reg_no' : self.validated_data.get('reg_no', ''),
                'address' : self.validated_data.get('address', ''),
                'password_at_time_of_creation' : self.validated_data.get('password_at_time_of_creation', ''),
                'imagepath' : self.validated_data.get('imagepath', ''),
                'section_id' : self.validated_data.get('section_id', ''),
                'class_id' : self.validated_data.get('class_id', ''),
                'contact_no' : self.validated_data.get('contact_no', ''),
                'school' : self.validated_data.get('school', ''),
            }
            data.update(extra_data)
            print(data)
            return data

    def save(self, request): #from rest_auth library code
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        #admin can addd student only in their school (if admin_id is present in school)
        admin = get_user_from_token(request)
        school_instance = self.cleaned_data.get('school')
        if admin.id == school_instance.admin.id: 
            adapter.save_user(request, user, self)
            self.custom_signup(request, user)
            setup_user_email(request, user, [])

            user.is_student = True
            user.save()
            try:
                student = StudentModel(student=user, name=self.cleaned_data.get('name'),
                    reg_no=self.cleaned_data.get('reg_no'),
                    address=self.cleaned_data.get('address'),
                    password_at_time_of_creation=self.cleaned_data.get('password_at_time_of_creation'),
                    imagepath=self.cleaned_data.get('imagepath'),section_id=self.cleaned_data.get('section_id'),class_id=self.cleaned_data.get('class_id'),
                    contact_no=self.cleaned_data.get('contact_no'), school=self.cleaned_data.get('school'))
                student.save()
                return user
            except Exception as e:
                print("Exception", e)
                user.delete()
                raise PermissionDenied('Something went wrong')
                # return Response({'message':'Some thing wents wrong. Please try again'}, status=HTTP_400_BAD_REQUEST)
        else:
            raise PermissionDenied('You are not the administrator of this school')

class ViewStudentSerializer(serializers.ModelSerializer):
    school = serializers.StringRelatedField(read_only=True)
    student = serializers.SerializerMethodField()

    class Meta:
        model = StudentModel
        fields = '__all__'

        # fields = fields = ['student' ,'name', 'reg_no', 'address','school' , 'imagepath' , 'contact_no', 'section_id', 'slug' ,'created_at', 'updated_at']

    def get_student(self,obj):
        return {
            "student_email": obj.student.email,
            }


class TeacherRegisterationSerializer(serializers.ModelSerializer,RegisterSerializer):
    teacher = serializers.PrimaryKeyRelatedField(read_only=True,)

    class Meta:
        model = TeacherModel
        fields = '__all__'

    def get_cleaned_data(self): #customization of rest_auth library code
            data = super(TeacherRegisterationSerializer, self).get_cleaned_data()
            extra_data = {
                'name' : self.validated_data.get('name', ''),
                'address' : self.validated_data.get('address', ''),
                # 'password_at_time_of_creation' : self.validated_data.get('password_at_time_of_creation', ''),
                'image' : self.validated_data.get('image', ''),
                'designation' : self.validated_data.get('designation', ''),
                'contact_no' : self.validated_data.get('contact_no', ''),
                'school' : self.validated_data.get('school', ''),
                'teacher_id' : self.validated_data.get('teacher_id', ''),
            }
            data.update(extra_data)
            print(data)
            return data

    def save(self, request): #from rest_auth library code
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        #admin can addd teacher only in their school (if admin_id is present in school)
        admin = get_user_from_token(request)
        school_instance = self.cleaned_data.get('school')
        if admin.id == school_instance.admin.id: 
            adapter.save_user(request, user, self)
            self.custom_signup(request, user)
            setup_user_email(request, user, [])

            user.is_teacher = True
            user.save()
            try:
                teacher = TeacherModel(teacher=user, name=self.cleaned_data.get('name')
                    ,address=self.cleaned_data.get('address'),
                    # password_at_time_of_creation=self.cleaned_data.get('password_at_time_of_creation'),
                    image=self.cleaned_data.get('image'),designation=self.cleaned_data.get('designation'),
                    contact_no=self.cleaned_data.get('contact_no'), school=self.cleaned_data.get('school'))
                teacher.save()
                return user
            except:
                user.delete()
                return Response({'message':'Some thing wents wrong. Please try again'}, status=HTTP_400_BAD_REQUEST)
        else:
            raise PermissionDenied('You are not the administrator of this school')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_superuser','is_administrator','is_teacher','is_student','is_client']


class AdminProfileSerializer(serializers.ModelSerializer):
    admin = serializers.SerializerMethodField()

    class Meta:
        model = SchoolModel
        fields = ['admin' ,'title', 'image', 'address', 'contact_no', 'created_at','updated_at']

    def get_admin(self,obj):
        return {
            "admin email": obj.admin.email,
            "Admin" : obj.admin.is_administrator
            }

class EnrollParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroll_ParentModel
        fields = '__all__'


class ParentRegisterationSerializer(serializers.ModelSerializer,RegisterSerializer):
    parent = serializers.PrimaryKeyRelatedField(read_only=True,)

    class Meta:
        model = ParentModel
        fields = '__all__'

    def get_cleaned_data(self): #customization of rest_auth library code
            data = super(ParentRegisterationSerializer, self).get_cleaned_data()
            extra_data = {
                'name': self.validated_data.get('name', ''),
                'password_at_time_of_creation' : self.validated_data.get('password_at_time_of_creation', ''),
                'imagepath' : self.validated_data.get('imagepath', ''),
                'contact_no' : self.validated_data.get('contact_no', ''),
                'school' : self.validated_data.get('school', ''),
            }
            data.update(extra_data)
            print(data)
            return data

    def save(self, request): #from rest_auth library code
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        #admin can addd student only in their school (if admin_id is present in school)
        admin = get_user_from_token(request)
        school_instance = self.cleaned_data.get('school')
        if admin.id == school_instance.admin.id: 
            adapter.save_user(request, user, self)
            self.custom_signup(request, user)
            setup_user_email(request, user, [])

            user.is_parent = True
            user.save()
            try:
                parent = ParentModel(parent=user, name=self.cleaned_data.get('name'),
                    password_at_time_of_creation=self.cleaned_data.get('password_at_time_of_creation'),
                    imagepath=self.cleaned_data.get('imagepath'),
                    contact_no=self.cleaned_data.get('contact_no'), school=self.cleaned_data.get('school'))
                parent.save()
                return user
            except Exception as e:
                print("Exception", e)
                user.delete()
                raise PermissionDenied('Something went wrong')
                # return Response({'message':'Some thing wents wrong. Please try again'}, status=HTTP_400_BAD_REQUEST)
        else:
            raise PermissionDenied('You are not the administrator of this school')


class ViewEnrollParentSerializer(serializers.ModelSerializer):
    parent = serializers.StringRelatedField(read_only = True)
    classes = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()

    def get_course(self,obj):
        return {
            "course_id": obj.course.id,
            "course": obj.course.title,
            }
    
    def get_classes(self,obj):
        return {
            "class_id": obj.classes.id,
            "class": obj.classes.title,
            }


    class Meta:
        model = Enroll_ParentModel
        fields = '__all__'
