
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.forms.formsets import formset_factory
from django.utils.timezone import datetime
from adminapp.models import *

# ***************** API ****************
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from django.http import Http404
from .serializers import *
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly, AllowAny
from adminapp.serializers import ViewAssignCourseSerializer
from superadmin.custompermissions import *
from superadmin.serializers import *
from superadmin.models import ArticleModel
from teacherApp.permissions import IsTeacher
from Student.views import ViewAndSubmitFeedback, is_enrolled_in_course_and_class
from Student.serializers import AssignmentSerializer
from django.contrib.auth import get_user_model
from adminapp.models import TeacherModel

User = get_user_model()

def get_user_from_token(request):
	token = request.user.auth_token #auth key(token) of current user 91391f4c12b94b753d08008150d2315d9d8d7e1e
	print("token.user_id",token.user_id) #gives id of user (pk)  2
	user = User.objects.get(id=token.user_id) #gives user name
	return user

def is_assgined_a_course_or_class(teacher, class_id, course_id):
    '''Check teacher is assigned a particular class/course or not'''
    assigned_course_teacher = Assign_TeacherModel.objects.filter(teacher__teacher=teacher)
    # print(assigned_course_teacher)
    # print(teacher)
    if assigned_course_teacher.exists():
        #get all classes and courses which is assigned to particular teacher
        assigned_courses_id = []
        assigned_classes_id = []

        for i in assigned_course_teacher:
            assigned_courses_id.append(i.course.id)
            assigned_classes_id.append(i.classes.id)
        #if requested course and class is assigned to a teacher then return True
        # print(assigned_courses_id)
        # print(assigned_classes_id)
        if course_id in assigned_courses_id and class_id in assigned_classes_id:
            return True
        else:
            return False
    else:
        return False


def is_assgined_a_course(teacher, course_id):
    '''Check teacher is assigned a particular class/course or not'''
    assigned_course_teacher = Assign_TeacherModel.objects.filter(teacher__teacher=teacher)
    # print(assigned_course_teacher)
    # print(teacher)
    if assigned_course_teacher.exists():
        #get all classes and courses which is assigned to particular teacher
        assigned_courses_id = []

        for i in assigned_course_teacher:
            assigned_courses_id.append(i.course.id)
        #if requested course and class is assigned to a teacher then return True
        # print(assigned_courses_id)
        # print(assigned_classes_id)
        if course_id in assigned_courses_id:
            return True
        else:
            return False
    else:
        return False


class ViewAssignedCoursesAndClass(generics.ListAPIView):
    '''Authenticated teachers can see their assigned courses'''
    permission_classes = (IsTeacher, )
    serializer_class = ViewAssignCourseSerializer

    def get_queryset(self):
        return Assign_TeacherModel.objects.filter(teacher__teacher=self.request.user.id)

class AddAssignment(APIView):
    '''
    Post: Teacher can add assignments in their assigned courses/classes
    GET: Teacher can see all assignment categorized into class/course 
    '''
    permission_classes = (IsTeacher,)

    def get(self, request, *args, **kwargs):
        #teacher can view the assignments of their assigned courses
        teacher = self.request.user
        Class = self.kwargs['class_id']
        course = self.kwargs['course_id']
        if is_assgined_a_course_or_class(teacher, Class, course):
            assignment = AssignmentModel.objects.filter(
                Class = self.kwargs['class_id'],
                course = self.kwargs['course_id'],
                teacher__teacher = self.request.user
                )
            serializer = AssignmentSerializer(assignment, many = True)
            return Response(serializer.data,status = status.HTTP_200_OK)
        else:
            return Response(
                {'message':'This course is not assigned to you'}, 
                status=status.HTTP_400_BAD_REQUEST
                )

    def get_teacher_instance(self):
        teacher = TeacherModel.objects.get(teacher=self.request.user.id)
        return teacher

    def post(self, request, *args, **kwargs):
        teacher = self.request.user
        Class = self.kwargs['class_id'],
        course = self.kwargs['course_id']
        if is_assgined_a_course_or_class(teacher, Class, course):
            serializer = AssignmentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(teacher=self.get_teacher_instance(), 
                    course=ViewAndSubmitFeedback.get_course_instance(self),
                    Class = ViewAndSubmitFeedback.get_class_instance(self))
                return Response(serializer.data,status = status.HTTP_201_CREATED)
            else:
                return Response(serializer.data,status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {'message':'This course is not assigned to you'}, 
                status=status.HTTP_400_BAD_REQUEST
                )

class DetailAssignment(APIView):
    permission_classes = (IsTeacher,)

    def get_object(self, slug):
        try:
            return AssignmentModel.objects.get(slug=slug)
        except AssignmentModel.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        #teacher can see their own assignments (object permission)
        data = self.get_object(slug)
        if data.teacher.teacher.id == request.user.id:
            serializer = AssignmentSerializer(data)
            return Response(serializer.data)
        else:
            return Response(
                {'message':'This course is not assigned to you'}, 
                status=status.HTTP_400_BAD_REQUEST
                )

    def delete(self, request, slug, format=None):
        #object permission
        assignement = self.get_object(slug)
        if assignement.teacher.teacher.id == request.user.id:
            assignement.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {'message':'You cannot delete this assignment'}, 
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, slug, format=None):
        #object permission
        assignement = self.get_object(slug)
        if assignement.teacher.teacher.id == request.user.id:
            serializer = AssignmentSerializer(assignement, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {'message':'You dont have right to update this assignment'}, 
                status=status.HTTP_400_BAD_REQUEST
                )

class AddLecture(APIView):
    permission_classes = (IsTeacher,)

    def post(self,request,format=None):
        #teacher can add lecture in their assigned courses
        serializer = lectureSerializer(data=request.data)
        if serializer.is_valid():
            Class = serializer.validated_data.get('Class', '').id
            course = serializer.validated_data.get('course', '').id
            if is_assgined_a_course_or_class(self.request.user, Class, course):
                serializer.save(teacher=AddAssignment.get_teacher_instance(self))
                return Response(serializer.data,status =status.HTTP_201_CREATED)
            else:
                return Response({"This course is not assigned to you"}, status =status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)


class ListLectureCourseWise(APIView):
    '''teacher can view the lectures of their assigned courses/classes'''
    def get(self, request, *args, **kwargs):
        teacher = self.request.user
        Class = self.kwargs['class_id']
        course = self.kwargs['course_id']
        if is_assgined_a_course_or_class(teacher, Class, course):
            lecture = AssignmentModel.objects.filter(
                Class = Class,
                course = course,
                )
            serializer = AssignmentSerializer(lecture, many = True)
            return Response(serializer.data,status = status.HTTP_200_OK)
        else:
            return Response(
                {'message':'This course is not assigned to you'}, 
                status=status.HTTP_400_BAD_REQUEST
                )


class LectureDetail(APIView):
    permission_classes = (IsTeacher, )

    def get_object(self,slug):
        try:
            return LectureModel.objects.get(slug=slug)
        except:
            raise Http404

    def get(self,request,slug,format=None):
        #assigned teachers can view lecture details
        data = self.get_object(slug)
        course = data.course.id
        Class = data.Class.id
        if is_assgined_a_course_or_class(self.request.user, Class, course):
            serializer = lectureSerializer(data)
            return Response(serializer.data)
        else:
            return Response(
                {'message':'This course is not assigned to you'}, 
                status=status.HTTP_400_BAD_REQUEST
                )


    def put(self,request,slug,format=None):
        #obj permission
        data = self.get_object(slug)
        if data.teacher.teacher == self.request.user:
            serializer = EditlectureSerializer(data, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
             return Response(
                {'message':'You dont have right to update this lecture'}, 
                status=status.HTTP_400_BAD_REQUEST
                )

    def delete(self,request,slug,format=None):
        #obj permission
        data = self.get_object(slug)
        if data.teacher.teacher.id == self.request.user:
            data.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {'message':'You dont have right to delete this lecture'}, 
                status=status.HTTP_400_BAD_REQUEST
                )


class Addtest(APIView):
    permission_classes = (IsTeacher, )
    def post(self,request,format=None):

        serializer = testSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            Class = serializer.validated_data.get('classes', '').id
            course = serializer.validated_data.get('course', '').id
            print(Class)
            print(course)
            if is_assgined_a_course_or_class(self.request.user, Class, course):
                serializer.save()
                return Response(serializer.data,status =status.HTTP_201_CREATED)
            else:
                return Response({"This course is not assigned to you"}, status =status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)


class Viewtest(APIView):
    permission_classes = (IsTeacher, )
    
    def get(self, request, *args, **kwargs):
        teacher = self.request.user
        Class = self.kwargs['class_id']
        course = self.kwargs['course_id']
        if is_assgined_a_course_or_class(teacher, Class, course):
            data = TestModel.objects.filter(
                    course = course, classes = Class
                )
            serializer = testSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )


class testDetail(APIView):
    permission_classes = (IsTeacher, )

    def get_object(self,slug):
        try:
            return TestModel.objects.get(slug=slug)
        except:
            raise Http404

    def get(self,request,slug,format=None):
        data = self.get_object(slug)
        course = data.course.id
        Class = data.classes.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            serializer = testSerializer(data)
            return Response(serializer.data)
        else:
            return Response(
                {'message':'This course is not assigned to you'}, 
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self,request,slug,format=None):
        data = self.get_object(slug)
        course = data.course.id
        Class = data.classes.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            serializer = testSerializer(data,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
        
        
    def delete(self,request,slug,format=None):
        data = self.get_object(slug)
        course = data.course.id
        Class = data.classes.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            data.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {'message':'This course is not assigned to you'}, 
                status=status.HTTP_400_BAD_REQUEST
                )

class Feedback(APIView):
    permission_classes = (IsTeacher, )

    def get(self, request, *args, **kwargs):
        #teacher can view the feedback of their assigned courses
        teacher = self.request.user
        Class = self.kwargs['class_id']
        course = self.kwargs['course_id']
        if is_assgined_a_course_or_class(teacher, Class, course):
            data = StudentFeedBackModel.objects.filter(
                course = course,
                Class = Class
            )
            serializer = StudentFeedbackSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {'message':'This course is not assigned to you'}, 
                status=status.HTTP_400_BAD_REQUEST
                )


class FeedbackDetail(APIView):
    permission_classes = (IsTeacher, )

    def get_object(self,pk):
        try:
            return StudentFeedBackModel.objects.get(id=pk)
        except:
            raise Http404

    def get(self,request,pk):
        #teacher can see the feedback detail of their asssigned courses
        data = self.get_object(pk)
        course = data.course.id
        Class = data.Class.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            serializer = StudentFeedbackSerializer(data)
            return Response(serializer.data)
        else:
            return Response(
                {'message':'This course is not assigned to you'}, 
                status=status.HTTP_400_BAD_REQUEST
                )



class Discussion(APIView):
    permission_classes = (IsTeacher, )
    
    def get(self, request, *args, **kwargs):
        #teacher can view the discussion of their assigned courses and classes
        teacher = self.request.user
        Class = self.kwargs['class_id']
        course = self.kwargs['course_id']
        if is_assgined_a_course_or_class(teacher, Class, course):
            data = DiscussionModel.objects.filter(
                course = course, Class = Class
            )
            serializer = DiscussionSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {'message':'This course is not assigned to you'}, 
                status=status.HTTP_400_BAD_REQUEST
                )


class AnsDiscussion(APIView):
    permission_classes = (IsAuthenticated, )

    def get_object(self,slug):
        try:
            return DiscussionModel.objects.get(slug=slug)
        except:
            raise Http404

    def post(self,request,slug,format=None):
        #teacher and students of assigned courses and classes can reply to the discussion
        data = self.get_object(slug)

        if request.user.is_student or request.user.is_teacher:
            course = data.course.id
            Class = data.Class.id

            if request.user.is_student:
                is_enrolled = is_enrolled_in_course_and_class(self.request.user,Class,course)
                if is_enrolled == True:
                    serializer = DiscussionAnswerSerializer(data=request.data)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save(
                            discussion = data,
                            student=ViewAndSubmitFeedback.get_student_instance(self)
                            )
                        return Response(serializer.data,status = status.HTTP_201_CREATED)
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(
                        {'message':'You are not enrolled in this course or class'}, 
                        status=status.HTTP_400_BAD_REQUEST
                        )
                
            elif request.user.is_teacher:
                if is_assgined_a_course_or_class(self.request.user, Class, course):
                    serializer = DiscussionAnswerSerializer(data=request.data)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save(
                            discussion = data,
                            teacher=AddAssignment.get_teacher_instance(self)
                        )
                        return Response(serializer.data,status = status.HTTP_201_CREATED)
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(
                        {'message':'This course is not assined to you'}, 
                        status=status.HTTP_400_BAD_REQUEST
                        )
        else:
            return Response(
                {'message':'Not Allowed'}, 
                status=status.HTTP_400_BAD_REQUEST
                )
        

class AddCalender(APIView):
    permission_classes = (IsTeacher, )

    def post(self,request,format=None):
        serializer = calenderSerializer(data=request.data)
        if serializer.is_valid():
            Class = serializer.validated_data.get('classes', '').id
            course = serializer.validated_data.get('course', '').id
            if is_assgined_a_course_or_class(self.request.user, Class, course):
                serializer.save()
                return Response(serializer.data,status =status.HTTP_201_CREATED)
            else:
                return Response({"This course is not assigned to you"}, status =status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)


class ViewCalender(APIView):
    permission_classes = (IsTeacher, )
    
    def get(self, request, *args, **kwargs):
    #teacher can view the calender of their courses
        teacher = self.request.user
        Class = self.kwargs['class_id']
        course = self.kwargs['course_id']
        if is_assgined_a_course_or_class(teacher, Class, course):
            data = CalenderModel.objects.filter(
                    course = course, classes = Class
                )
            serializer = calenderSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )


class CalenderDetail(APIView):
    permission_classes = (IsTeacher, )

    def get_object(self,slug):
        try:
            return CalenderModel.objects.get(slug=slug)
        except:
            raise Http404

    def get(self,request,slug,format=None):
        data = self.get_object(slug)
        course = data.course.id
        Class = data.classes.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            serializer = calenderSerializer(data)
            return Response(serializer.data)
        else:
            return Response(
                {'message':'This course is not assigned to you'}, 
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self,request,slug,format=None):
        #teachers can update the calender of their assigned courses (no obj permission)
        data = self.get_object(slug)
        course = data.course.id
        Class = data.classes.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            serializer = EditcalenderSerializer(data,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
        
        
    def delete(self,request,slug,format=None):
        data = self.get_object(slug)
        course = data.course.id
        Class = data.classes.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            data.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {'message':'This course is not assigned to you'}, 
                status=status.HTTP_400_BAD_REQUEST
                )


class AddQuiz(APIView):
    permission_classes = (IsTeacher, )

    def post(self,request,format=None):
        serializer = createquizSerializer(data=request.data)
        # print(serializer)
        if serializer.is_valid():
            Class = serializer.validated_data.get('classes', '').id
            course = serializer.validated_data.get('course', '').id
            # print(course)
            # print(Class)
            if is_assgined_a_course_or_class(self.request.user, Class, course):
                serializer.save()
                return Response(serializer.data,status =status.HTTP_201_CREATED)
            else:
                return Response({"This course is not assigned to you"}, status =status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)


class ViewQuiz(APIView):
    permission_classes = (IsTeacher, )
    
    def get(self, request, *args, **kwargs):
        teacher = self.request.user
        Class = self.kwargs['class_id']
        course = self.kwargs['course_id']
        if is_assgined_a_course_or_class(teacher, Class, course):
            data = createQuizModel.objects.filter(
                    course = course, classes = Class
                )
            serializer = createquizSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )



class QuizDetail(APIView):
    permission_classes = (IsTeacher, )

    def get_object(self,slug):
        try:
            return createQuizModel.objects.get(slug=slug)
        except:
            raise Http404

    def get(self,request,slug,format=None):
        data = self.get_object(slug)
        course = data.course.id
        Class = data.classes.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            serializer = createquizSerializer(data)
            return Response(serializer.data)
        else:
            return Response(
                {'message':'This course is not assigned to you'}, 
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self,request,slug,format=None):
        data = self.get_object(slug)
        course = data.course.id
        Class = data.classes.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            serializer = EditquizSerializer(data,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
        
        
    def delete(self,request,slug,format=None):
        data = self.get_object(slug)
        course = data.course.id
        Class = data.classes.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            data.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {'message':'This course is not assigned to you'}, 
                status=status.HTTP_400_BAD_REQUEST
                )


class AddQuestion(APIView):
    permission_classes = (IsTeacher, )

    def post(self,request,format=None):
        serializer = questionSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            course = serializer.validated_data.get('course', '').id
            
            if is_assgined_a_course(self.request.user, course):
                serializer.save()
                return Response(serializer.data,status =status.HTTP_201_CREATED)
            else:
                return Response({"This course is not assigned to you"}, status =status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)



class ViewQuestion(APIView):
    permission_classes = (IsTeacher, )
    
    def get(self, request, *args, **kwargs):
        teacher = self.request.user
        Class = self.kwargs['class_id']
        course = self.kwargs['course_id']
        if is_assgined_a_course_or_class(teacher, Class, course):
            data = quizQuestionsAndAnswersModel.objects.filter(
                    course = course, classes = Class
                )
            serializer = questionSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )



class QuestionDetail(APIView):
    permission_classes = (IsTeacher, )

    def get_object(self,slug):
        try:
            return quizQuestionsAndAnswersModel.objects.get(slug=slug)
        except:
            raise Http404

    def get(self,request,slug,format=None):
        data = self.get_object(slug)
        course = data.course.id
        Class = data.classes.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            serializer = questionSerializer(data)
            return Response(serializer.data)
        else:
            return Response(
                {'message':'This course is not assigned to you'}, 
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self,request,slug,format=None):
        data = self.get_object(slug)
        course = data.course.id
        Class = data.classes.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            serializer = questionSerializer(data,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
        
        
    def delete(self,request,slug,format=None):
        data = self.get_object(slug)
        course = data.course.id
        Class = data.classes.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            data.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {'message':'This course is not assigned to you'}, 
                status=status.HTTP_400_BAD_REQUEST
                )


class SubmittedTestView(APIView):
    #teacher can view the submitted test of their course or class (obj perm)
    permission_classes = (IsTeacher, )
    
    def get(self, request, *args, **kwargs):
        teacher = self.request.user
        Class = self.kwargs['class_id']
        course = self.kwargs['course_id']
        if is_assgined_a_course_or_class(teacher, Class, course):
            data = SubmittestModel.objects.filter(
                test__Class = Class,
                test__course = course,
                test__teacher__teacher = teacher
            )
            serializer = submittedtestSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )


class SubmittedQuestionView(APIView):
    #teacher can view the submitted question of their course or class (obj perm)
    permission_classes = (IsTeacher, )
    
    def get(self, request, *args, **kwargs):
        teacher = self.request.user
        Class = self.kwargs['class_id']
        course = self.kwargs['course_id']
        if is_assgined_a_course_or_class(teacher, Class, course):
            data = SubmitquestionModel.objects.filter(
                question__Class = Class,
                question__course = course,
                question__teacher__teacher = teacher
            )
            serializer = submittedquestionSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )


class AddResultView(APIView):
    permission_classes = (IsTeacher, )

    def post(self,request):
        #teacher can post the results of students enrolled in their assigned course
        serializer = resultSerializer(data = request.data)
        if serializer.is_valid():
            Class = serializer.validated_data.get('Class', '').id
            course = serializer.validated_data.get('course', '').id
            student = serializer.validated_data.get('student', '').student
            if is_assgined_a_course_or_class(self.request.user, Class, course):
                #check student is enrolled in a course or not
                if is_enrolled_in_course_and_class(student,Class,course):
                    serializer.save()
                    return Response(serializer.data,status =status.HTTP_201_CREATED)
                else:
                    return Response({"message":"This student is not enrolled in this course"},
                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
        else:
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)


class ViewResults(APIView):
    #teachers can view the results of their assigned courses
    permission_classes = (IsTeacher, )
    
    def get(self, request, *args, **kwargs):
        teacher = self.request.user
        Class = self.kwargs['class_id']
        course = self.kwargs['course_id']
        if is_assgined_a_course_or_class(teacher, Class, course):
            data = ResultModel.objects.filter(
                    course = course, Class = Class
                )
            serializer = ViewResultSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )


class DetailResultView(APIView):
    permission_classes = (IsTeacher, )

    def get_object(self,pk):
        try:
            return ResultModel.objects.get(id=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        #teacher can view the detail of results of their assigned courses
        data = self.get_object(pk)
        course = data.course.id
        Class = data.Class.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            serializer = ViewResultSerializer(data)
            return Response(serializer.data)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )


    def put(self,request,pk,format=None):
        #teacher can update the detail of results of their assigned courses (no obj perm)
        data = self.get_object(pk)
        course = data.course.id
        Class = data.Class.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            serializer = ViewResultSerializer(data,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
             return Response(
                        {'message':'This course is not assigned to you'}, 
                        status=status.HTTP_400_BAD_REQUEST
                        )

    def delete(self,request,pk,format=None):
        data = self.get_object(pk)
        course = data.course.id
        Class = data.Class.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            data.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )


class SubmittedAssignmentView(APIView):
    #teacher can view the submitted assignment of their course or class (obj perm)
    permission_classes = (IsTeacher, )
    
    def get(self, request, *args, **kwargs):
        teacher = self.request.user
        Class = self.kwargs['class_id']
        course = self.kwargs['course_id']
        if is_assgined_a_course_or_class(teacher, Class, course):
            data = SubmitAssignmentModel.objects.filter(
                assignment__Class = Class,
                assignment__course = course,
                assignment__teacher__teacher = teacher
            )
            serializer = submittedAssignmentSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )

#################################################


class TeacherProfileView(APIView):
    permission_classes = (IsTeacher, )

    def get_object(self,user):
        print(TeacherModel.objects.get(teacher = user))
        try:
            return TeacherModel.objects.get(teacher = user)
        except:
            raise Http404 

    def get(self, request, *args, **kwargs):
        user = get_user_from_token(request)
        # print(user)
        teacher = self.get_object(user)
        serializer = TeacherProfileSerializer(teacher)
        return Response(serializer.data)


class AddArticleView(generics.CreateAPIView):
    #All authenticated users can add articles
    permission_classes = (IsAuthenticated, )
    serializer_class = ArticleSerializer
    queryset = ArticleModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListArticleView(generics.ListAPIView):
    #Anyone can see the published Articles
    permission_classes = (AllowAny, )
    serializer_class = ArticleSerializer
    queryset = ArticleModel.objects.filter(status__exact="P")


class ArticleDetail(generics.RetrieveAPIView):
    #anyone can see detail of published article
    lookup_field = 'slug'
    permission_classes = (AllowAny, )
    serializer_class = ArticleSerializer
    queryset = ArticleModel.objects.filter(status__exact="P")
class AddAnnouncementView(APIView):
    permission_classes = (IsTeacher, )

    def post(self,request):
        #teacher can post the attendance of students enrolled in their assigned course
        serializer = TeacherAnnouncementSerializer(data = request.data)
        if serializer.is_valid():
            Class = serializer.validated_data.get('Class', '').id
            course = serializer.validated_data.get('course', '').id
            teacher=self.request.user
            if is_assgined_a_course_or_class(teacher, Class, course):
                serializer.save()
                return Response(serializer.data,status =status.HTTP_201_CREATED)
            else:
                return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
        else:
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)

class AnnouncementView(APIView):
    #teachers can view the Annoucement of their assigned courses
    permission_classes = (IsTeacher, )
    
    def get(self, request, *args, **kwargs):
        teacher = self.request.user
        Class = self.kwargs['class_id']
        course = self.kwargs['course_id']
        if is_assgined_a_course_or_class(teacher, Class, course):
            data = TeacherAnnouncementModel.objects.filter(
                    course = course, Class = Class
                )
            serializer = TeacherAnnouncementSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )                        
                                         
                               


class DetailAnnouncementView(APIView):
    permission_classes = (IsTeacher, )

    def get_object(self,pk):
        try:
            return TeacherAnnouncementModel.objects.get(id=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        #teacher can view the detail of Announcement of their assigned courses
        data = self.get_object(pk)
        course = data.course.id
        Class = data.Class.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            serializer = ViewAnnoucementSerializer(data)
            return Response(serializer.data)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )


    def put(self,request,pk,format=None):
        #teacher can update the detail of Annoucement of their assigned courses (no obj perm)
        data = self.get_object(pk)
        course = data.course.id
        Class = data.Class.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            serializer = ViewAnnoucementSerializer(data,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
             return Response(
                        {'message':'This course is not assigned to you'}, 
                        status=status.HTTP_400_BAD_REQUEST
                        )

    def delete(self,request,pk,format=None):
        data = self.get_object(pk)
        course = data.course.id
        Class = data.Class.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            data.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )                   

class AddStudentAttendanceView(APIView):
    permission_classes = (IsTeacher, )

    def post(self,request):
        #teacher can post the attendance of students enrolled in their assigned course
        serializer = StudentAttendanceSerializer(data = request.data)
        if serializer.is_valid():
            Class = serializer.validated_data.get('Class', '').id
            course = serializer.validated_data.get('course', '').id
            student = serializer.validated_data.get('student', '').student
            teacher=self.request.user
            if is_assgined_a_course_or_class(teacher, Class, course):
                #check student is enrolled in a course or not
                if is_enrolled_in_course_and_class(student,Class,course):
                    serializer.save()
                    return Response(serializer.data,status =status.HTTP_201_CREATED)
                else:
                    return Response({"message":"This student is not enrolled in this course"},
                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
        else:
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)

class DetailStudentAttendanceView(APIView):
    permission_classes = (IsTeacher, )

    def get_object(self,pk):
        try:
            return StudentAttendanceModel.objects.get(id=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        #teacher can view the detail of Attendance of their assigned courses
        data = self.get_object(pk)
        course = data.course.id
        Class = data.Class.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            serializer = ViewAttendanceSerializer(data)
            return Response(serializer.data)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )


    def put(self,request,pk,format=None):
        #teacher can update the detail of Attendance of their assigned courses (no obj perm)
        data = self.get_object(pk)
        course = data.course.id
        Class = data.Class.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            serializer = ViewAttendanceSerializer(data,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
             return Response(
                        {'message':'This course is not assigned to you'}, 
                        status=status.HTTP_400_BAD_REQUEST
                        )
    def delete(self,request,pk,format=None):
        data = self.get_object(pk)
        course = data.course.id
        Class = data.Class.id
        teacher = self.request.user
        if is_assgined_a_course_or_class(teacher, Class, course):
            data.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )                   
class ViewAttendance(APIView):
    #teachers can view the results of their assigned courses
    permission_classes = (IsTeacher, )
    
    def get(self, request, *args, **kwargs):
        teacher = self.request.user
        Class = self.kwargs['class_id']
        course = self.kwargs['course_id']
        if is_assgined_a_course_or_class(teacher, Class, course):
            data = StudentAttendanceModel.objects.filter(
                    course = course, Class = Class
                )
            serializer = ViewAttendanceSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                    {'message':'This course is not assigned to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )                        
                   