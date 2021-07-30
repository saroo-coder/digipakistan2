from rest_framework import serializers
from .models import *
from teacherApp.models import AssignmentModel
from adminapp.models import ContactFormModel, StudentModel
from superadmin.serializers import CourseSerializer, QuestionSerializer, DiscussionSerializer

class AssignmentSerializer(serializers.ModelSerializer):
    Class = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()
    teacher = serializers.SerializerMethodField()

    class Meta:
        model = AssignmentModel
        fields = '__all__'

    def get_Class(self,obj):
        return {
            "class": obj.Class.title,
            }
    
    def get_course(self,obj):
        return {
            "course": obj.course.title,
            }

    def get_teacher(self,obj):
        return {
            "teacher": obj.teacher.name,
            }


class ComplainSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ContactFormModel
        fields = ['student','query','updated_at']


class StudentProfileSerializer(serializers.ModelSerializer):
    school = serializers.StringRelatedField(read_only=True)
    student = serializers.SerializerMethodField()

    class Meta:
        model = StudentModel
        fields = ['student' ,'name', 'reg_no', 'address','school' , 'imagepath' , 'contact_no', 'section_id', 'slug' ,'created_at', 'updated_at']

    def get_student(self,obj):
        return {
            "student email": obj.student.email,
            "Student" : obj.student.is_student
            }

