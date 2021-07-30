from rest_framework import serializers
from .models import *
from adminapp.serializers import AssignCourseSerializer
from superadmin.serializers import CourseSerializer, QuestionSerializer


class lectureSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = LectureModel
        fields = '__all__'

class EditlectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureModel
        fields = ['title','tutorial_link','notes','recorded_lecture','description']

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesModel
        fields = ('__all__')

class classSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblClassModel
        fields = ('__all__')

class calenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalenderModel
        fields = '__all__'

class EditcalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalenderModel
        fields = ['title','details','due_date']

class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = '__all__'

class StudentFeedbackSerializer(serializers.ModelSerializer):
    Class = serializers.StringRelatedField(read_only=True,)
    course = serializers.StringRelatedField(read_only=True,)
    student = serializers.StringRelatedField(read_only=True,)
    # teacher = teacherSerializer(read_only=True, many=True)
    class Meta:
        model = StudentFeedBackModel
        fields = '__all__'


class ParentFeedbackSerializer(serializers.ModelSerializer):
    Class = serializers.StringRelatedField(read_only=True,)
    course = serializers.StringRelatedField(read_only=True,)
    parent = serializers.StringRelatedField(read_only=True,)
    # teacher = teacherSerializer(read_only=True, many=True)
    class Meta:
        model = ParentFeedBackModel
        fields = '__all__'

class DiscussionSerializer(serializers.ModelSerializer):
    answers = serializers.SlugRelatedField( many=True,
        read_only=True,
        slug_field='reply')
    Class = serializers.PrimaryKeyRelatedField(read_only=True,)
    course = serializers.PrimaryKeyRelatedField(read_only=True,)
    student = serializers.StringRelatedField(read_only=True,)
    class Meta:
        model = DiscussionModel
        fields =  ['Class', 'course', 'student','content','slug','created_at','answers']

class DiscussionAnswerSerializer(serializers.ModelSerializer):
    discussion = serializers.PrimaryKeyRelatedField(read_only=True,)
    Class = serializers.PrimaryKeyRelatedField(read_only=True,)
    course = serializers.PrimaryKeyRelatedField(read_only=True,)
    student = serializers.StringRelatedField(read_only=True,)
    teacher = serializers.StringRelatedField(read_only=True,)
    class Meta:
        model = DiscussionAnswer
        fields = '__all__'

class createquizSerializer(serializers.ModelSerializer):
    # course = serializers.StringRelatedField(many=False)
    # classes = serializers.StringRelatedField(many=False)
    class Meta:
        model = createQuizModel
        fields = '__all__'


class EditquizSerializer(serializers.ModelSerializer):
    class Meta:
        model = quizQuestionsAndAnswersModel
        fields = ['title','question','answer']

class questionSerializer(serializers.ModelSerializer):
    class Meta:
        model = quizQuestionsAndAnswersModel
        fields =  '__all__'
        
class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = '__all__' 
        
class schoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolModel
        fields = '__all__' 


class testSerializer(serializers.ModelSerializer):
    # classes = serializers.StringRelatedField(many=False)
    # course = serializers.StringRelatedField(many=False)
    

    class Meta:
        model = testModel
        fields = '__all__'


class resultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultModel
        fields = '__all__'

class ViewResultSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField(read_only=True,)
    Class = serializers.StringRelatedField(read_only=True,)
    student = serializers.StringRelatedField(read_only=True,)
    class Meta:
        model = ResultModel
        fields = '__all__'


class submittedquestionSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(read_only=True,)
    student = serializers.PrimaryKeyRelatedField(read_only=True,)

    class Meta:
        model = SubmittestModel
        fields = '__all__'


class submittedtestSerializer(serializers.ModelSerializer):
    test = serializers.PrimaryKeyRelatedField(read_only=True,)
    student = serializers.PrimaryKeyRelatedField(read_only=True,)

    class Meta:
        model = SubmittestModel
        fields = '__all__'

class submittedAssignmentSerializer(serializers.ModelSerializer):
    assignment = serializers.PrimaryKeyRelatedField(read_only=True,)
    student = serializers.PrimaryKeyRelatedField(read_only=True,)

    class Meta:
        model = SubmitAssignmentModel
        fields = '__all__'

class AnnouncementSerializer(serializers.ModelSerializer):
    Class = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()
    teacher = serializers.SerializerMethodField()

    class Meta:
        model = AnnouncementModel
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



class TeacherProfileSerializer(serializers.ModelSerializer):
    school = serializers.StringRelatedField(read_only=True)
    teacher = serializers.SerializerMethodField()

    class Meta:
        model = TeacherModel
        fields  = ['teacher' ,'name', 'address','school' , 'image' , 'contact_no','designation', 'slug' ,'created_at', 'updated_at']

    def get_teacher(self,obj):
        return {
            "student email": obj.teacher.email,
            "Student" : obj.teacher.is_teacher
            }
class TeacherAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherAnnouncementModel
        fields = '__all__'

class ViewAnnouncementSerializer(serializers.ModelSerializer):
    Class = serializers.StringRelatedField(read_only=True,)
    course = serializers.StringRelatedField(read_only=True,)
    # teacher = teacherSerializer(read_only=True, many=True)
    class Meta:
        model = TeacherAnnouncementModel
        fields = '__all__' 

class StudentAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendanceModel
        fields = '__all__'

class ViewAttendanceSerializer(serializers.ModelSerializer):
    Class = serializers.StringRelatedField(read_only=True,)
    course = serializers.StringRelatedField(read_only=True,)
    student = serializers.StringRelatedField(read_only=True,)
    # teacher = teacherSerializer(read_only=True, many=True)
    class Meta:
        model = StudentAttendanceModel
        fields = '__all__'
