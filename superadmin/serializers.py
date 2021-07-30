from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_auth.registration.views import RegisterView
from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.contrib.auth import get_user_model, authenticate
from rest_framework.exceptions import PermissionDenied

User = get_user_model()

def get_user_from_token(request): 
    '''It will given the current username by using token'''
    token = request.user.auth_token
    user = User.objects.get(id=token.user_id)
    return user




class QuestionSerializer(serializers.ModelSerializer):
    # onlinetests = OnlineTestSerializer(many=True, read_only=True)
    class Meta:
        model = QuestionModel
        fields = '__all__'
class Client_submittedquestionSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(read_only=True,)
    client = serializers.PrimaryKeyRelatedField(read_only=True,)

    class Meta:
        model = Client_SubmitquestionModel
        fields = '__all__'       

class testSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_testModel
        fields = '__all__'

class Client_submittedtestSerializer(serializers.ModelSerializer):
    test = serializers.PrimaryKeyRelatedField(read_only=True,)
    client = serializers.PrimaryKeyRelatedField(read_only=True,)

    class Meta:
        model = Client_SubmittestModel
        fields = '__all__'    
        
class DiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionModel
        fields = '__all__'

# class OptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OptionModel
#         fields = '__all__'
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolModel
        fields = '__all__'


class RegisterSchoolSerializer(serializers.ModelSerializer,RegisterSerializer):
    school = serializers.PrimaryKeyRelatedField(read_only=True,)

    class Meta:
        model = SchoolModel
        fields = '__all__'

    def get_cleaned_data(self): 
            data = super(RegisterSchoolSerializer, self).get_cleaned_data()
            extra_data = {
                'title': self.validated_data.get('title', ''),
                'image' : self.validated_data.get('image', ''),
                'address' : self.validated_data.get('address', ''),
                'email' : self.validated_data.get('email', ''),
                'password' : self.validated_data.get('password', ''),
                'contact_no' : self.validated_data.get('contact_no', ''),
                }
            data.update(extra_data)
            print(data)
            return data

    def save(self, request): 
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        admin = get_user_from_token(request)
        adapter.save_user(request, user, self)
        user.save()
        try:
            school = SchoolModel(admin=user, title=self.cleaned_data.get('title'),
                image=self.cleaned_data.get('image'),
                address=self.cleaned_data.get('address'),
                email=self.cleaned_data.get('email'),
                password=self.cleaned_data.get('password'),
                contact_no=self.cleaned_data.get('contact_no'))
            school.save()
            return user
        except Exception as e:
            print("Exception", e)
            user.delete()
            raise PermissionDenied('Something went wrong')
        
class ArticleSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    class Meta:
        model = ArticleModel
        fields = ('__all__')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_user(self, obj):
        if obj.user.is_student:
            User = Enroll_StudentModel.objects.filter(student__student = obj.user)
            if User.exists():
                User = User[0]
                return {"user": User.student.student.username, "class": User.classes.title}
            else:
                return {"user": obj.user.username, "class": "None"}
        else:
            return obj.user.username


class UpdateArticleSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = ArticleModel
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ('__all__')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = '__all__'

class BusinessPartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessPartnersModel
        fields = ('__all__')

# class QueriesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = QueriesModel
#         fields = ('__all__')

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementModel
        fields = '__all__'
        
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomModel
        fields = ('__all__')

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleModel
        fields = ('__all__')


class ClientFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientFeedBackModel
        fields = ['id','course','description','client','rating','created_at']


class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CourseModel
        fields = ('__all__')

class ViewCourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CourseModel
        fields = ('__all__')

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CourseModel
        fields = ('__all__')
class EnrollCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroll_CourseModel
        fields = '__all__'


class ViewEnrollCourseSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField(read_only=True,)
    client = serializers.StringRelatedField(read_only=True,)
    class Meta:
        model = Enroll_CourseModel
        fields = '__all__'
class ViewComplainSerializer(serializers.ModelSerializer):   #Client-Complain
    class Meta:
        model = ClientComplainModel
        fields = ['id','client','query','created_at']


class submitComplainSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(read_only=True,)

    class Meta:
        model = ClientComplainModel
        fields = '__all__'


class AdvisoryBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvisoryBoardModel
        fields = ('__all__')

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamModel
        fields = ('__all__')


class BusinessPromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessPromotionModel
        fields = ('__all__')


class  KidTalentSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    class Meta:
        model = KidTalentModel
        fields = ('__all__')
    
    def get_status(self, obj):
        return obj.get_status_display()

    def get_user(self, obj):
        if obj.user.is_student:
            User = Enroll_StudentModel.objects.filter(student__student = obj.user)
            if User.exists():
                User = User[0]
                return {"user": User.student.student.username, "class": User.classes.title}
            else:
                return {"user": obj.user.username, "class": "None"}
        else:
            return obj.user.username


class UpdateKidsTalentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = KidTalentModel
        fields = ('__all__')

class  KidStorySerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    class Meta:
        model = KidStoryModel
        fields = ('__all__')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_user(self, obj):
        if obj.user.is_student:
            User = Enroll_StudentModel.objects.filter(student__student = obj.user)
            if User.exists():
                User = User[0]
                return {"user": User.student.student.username, "class": User.classes.title}
            else:
                return {"user": obj.user.username, "class": "None"}
        else:
            return obj.user.username


class UpdateKidsStorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = KidStoryModel
        fields = ('__all__')



class  QuizContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizContextModel
        fields = ('__all__')


class WebsiteAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteAdModel
        fields = ('__all__')


class CustomerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerReviewModel
        fields = ('__all__')


class JobClassifiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobClassifiedModel
        fields = ('__all__')
