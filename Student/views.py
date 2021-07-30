
# Create your views here.
from django.shortcuts import render
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# from django.contrib.auth import logout, authenticate, login
from rest_framework.exceptions import PermissionDenied

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import generics
from .permissions import *

# models
from teacherApp.models import *
from adminapp.models import TblClassModel, Enroll_StudentModel, ContactFormModel
from superadmin.models import ArticleModel

# serializers
from adminapp.serializers import ViewEnrollStudentSerializer, ResponseSerializer, ViewStudentSerializer
from Student.serializers import AssignmentSerializer, ComplainSerializer, StudentProfileSerializer
from teacherApp.serializers import *
from superadmin.serializers import ArticleSerializer
User = get_user_model()

def get_user_from_token(request):
	token = request.user.auth_token #auth key(token) of current user 91391f4c12b94b753d08008150d2315d9d8d7e1e
	print("token.user_id",token.user_id) #gives id of user (pk)  2
	user = User.objects.get(id=token.user_id) #gives user name
	return user
	


def is_enrolled_in_course_and_class(student,class_id,course_id):
        #check student is enrolled in given class or course.
        enrolled_student_data = Enroll_StudentModel.objects.filter(student__student = student)
        print(enrolled_student_data, class_id, course_id)
        if enrolled_student_data.exists():
            enrolled_courses_id = []
            enrolled_classes_id = []
            for enrolled_student in enrolled_student_data:
                enrolled_courses_id.append(enrolled_student.course.id)
                enrolled_classes_id.append(enrolled_student.classes.id)
            if course_id in enrolled_courses_id and class_id in enrolled_classes_id:
                return True
            else:
                return False
        else:
            return False

def is_enrolled_with_teacher(student,teacher_id):
        #check student is enrolled in given class or course.
        enrolled_student_data = Enroll_StudentModel.objects.filter(student__student = student)
        print(enrolled_student_data, teacher_id)
        if enrolled_student_data.exists():
            enrolled_teachers_id = []
            for enrolled_student in enrolled_student_data:
                enrolled_teachers_id.append(enrolled_student.teacher.id)
            if teacher_id in enrolled_teachers_id:
                return True
            else:
                return False
        else:
            return False


class ViewAssignment(generics.ListAPIView):
    '''Student can see the assignments of those courses and classess in which he/she is enrolled'''
    permission_classes = (IsStudent, )
    serializer_class = AssignmentSerializer
    
    def get(self, request, *args, **kwargs):
        student = request.user.id
        course_id = self.kwargs['course_id']
        class_id = self.kwargs["class_id"]
        #if student is enrolled in a class/course
        is_enrolled = is_enrolled_in_course_and_class(student,class_id,course_id)
        if is_enrolled == True:
            return self.list(request, *args, **kwargs)
        else:
            return Response(
                {'message':'You are not enrolled in this course or class'}, 
                status=HTTP_400_BAD_REQUEST
                )

    def get_queryset(self):
        return AssignmentModel.objects.filter(
            course=self.kwargs['course_id'],
            Class=self.kwargs['class_id']
            )


class ViewEnrolledCourses(generics.ListAPIView):
    '''Authenticated Student can see their enrolled courses'''
    permission_classes = (IsStudent, )
    serializer_class = ViewEnrollStudentSerializer

    def get_queryset(self):
        return Enroll_StudentModel.objects.filter(student__student=self.request.user.id)


class SubmitAssignment(generics.ListCreateAPIView):
    ''' if student is enrolled in a course and class whose assignment is assigned then he/she can submit th assignment'''
    permission_classes = (IsStudent, )
    serializer_class = submittedAssignmentSerializer

    def get_queryset(self):
        return SubmitAssignmentModel.objects.filter(
            assignment=self.kwargs['assignment_id'],
            student__student=self.request.user.id
            )

    def get_student_instance(self):
        student = StudentModel.objects.get(student=self.request.user.id)
        return student
        
    def perform_create(self, serializer):
        assignment = AssignmentModel.objects.get(id=self.kwargs['assignment_id'])
        student = self.request.user.id
        class_id = assignment.teacher.classes.id
        course_id = assignment.teacher.course.id
        #check student is enrolled in class/course or not.
        is_enrolled = is_enrolled_in_course_and_class(student,class_id,course_id)
        if is_enrolled == True:
            #if student have already submitted the assignment
            submit_assignment = SubmitAssignmentModel.objects.filter(
                student__student=student, assignment=assignment
                )
            if submit_assignment.exists():
                if submit_assignment[0].is_submit:
                    raise PermissionDenied('You have already submitted the assignment') 
            else:
                serializer.save(
                    student=self.get_student_instance(),
                    assignment=assignment, is_submit=True
                )
        elif is_enrolled == False:
            raise PermissionDenied('You cannot submit the assignment because you are not enrolled in this course') 


class ViewAndSubmitFeedback(generics.ListCreateAPIView):
    permission_classes = (IsStudent, )
    serializer_class = StudentFeedbackSerializer

    def get_queryset(self):
        return StudentFeedBackModel.objects.filter(
            course=self.kwargs['course_id'],
            Class=self.kwargs['class_id'],
            student__student= self.request.user.id
            )

    def get_student_instance(self):
        student = StudentModel.objects.get(student=self.request.user.id)
        return student

    def get_course_instance(self):
        course = CourseModel.objects.get(id=self.kwargs['course_id'])
        return course

    def get_class_instance(self):
        course = TblClassModel.objects.get(id=self.kwargs['class_id'])
        return course

    def perform_create(self, serializer):
        #check student is enrolled in a course or not
        student = self.request.user.id
        class_id = self.kwargs['class_id']
        course_id = self.kwargs['course_id']
        is_enrolled = is_enrolled_in_course_and_class(student,class_id,course_id)
        if is_enrolled == True:
            serializer.save(
                student=self.get_student_instance(),
                course=self.get_course_instance(), 
                Class=self.get_class_instance()
                )
        else:
            raise PermissionDenied('You are not enrolled in this course or class')


class ViewLectures(generics.ListAPIView):
    '''Student will see the lectures of those classes and course in which he/she is enrolled.'''
    permission_classes = (IsStudent, )
    serializer_class = lectureSerializer

    def get(self, request, *args, **kwargs):
        #check student is enrolled in a course or class
        student = self.request.user.id
        class_id = self.kwargs['class_id']
        course_id = self.kwargs['course_id']
        is_enrolled = is_enrolled_in_course_and_class(student,class_id,course_id)
        if is_enrolled == True:
            return self.list(request, *args, **kwargs)
        else:
            return Response(
                {'message':'You are not enrolled in this course or class'}, 
                status=HTTP_400_BAD_REQUEST
                )

    def get_queryset(self):
        return LectureModel.objects.filter(
            course=self.kwargs['course_id'], 
            Class=self.kwargs['class_id']
        )


# class ViewResults(generics.ListAPIView):
#     permission_classes = (IsStudent, )
#     serializer_class = resultSerializer

#     def get(self, request, *args, **kwargs):
#         return ViewLectures.get(self, request, *args, **kwargs)

#     def get_queryset(self):
#         return ResultModel.objects.filter(
#             course=self.kwargs['course_id'], 
#             Class=self.kwargs['class_id'], 
#             student__student=self.request.user.id
#             )


class LectureDetail(generics.ListAPIView):
    permission_classes = (IsStudent, )
    serializer_class = lectureSerializer

    def get(self, request, *args, **kwargs):
        return ViewLectures.get(self, request, *args, **kwargs)

    def get_queryset(self):
        return LectureModel.objects.filter(
            id=self.kwargs['lecture_id'], 
            course=self.kwargs['course_id'], 
            Class=self.kwargs['class_id']
            )


class DiscussionForm(generics.CreateAPIView):
    '''Student can post the queries about course'''
    permission_classes = (IsStudent, )
    serializer_class = DiscussionSerializer

    def get_student_instance(self):
        return ViewAndSubmitFeedback.get_student_instance(self)

    def get_course_instance(self):
        return ViewAndSubmitFeedback.get_course_instance(self)
        
    def get_class_instance(self):
        return ViewAndSubmitFeedback.get_class_instance(self)

    def perform_create(self, serializer):
        return ViewAndSubmitFeedback.perform_create(self, serializer)


class ListDiscussion(generics.ListAPIView):
    'All students enrolled in a course can see the queries'
    permission_classes = (IsStudent, )
    serializer_class = DiscussionSerializer

    def get(self, request, *args, **kwargs):
         #check student is enrolled in a course or class
        return ViewLectures.get(self, request, *args, **kwargs)

    def get_queryset(self):
        return DiscussionModel.objects.filter(
            course=self.kwargs['course_id'], 
            Class=self.kwargs['class_id']
            )


class SubmitComplain(generics.CreateAPIView):
    permission_classes = (IsStudent,)
    serializer_class = ComplainSerializer

    def perform_create(self, serializer):
        serializer.save(student=ViewAndSubmitFeedback.get_student_instance(self))


class ViewComplain(generics.ListAPIView):
    permission_classes = (IsStudent,)
    serializer_class = ComplainSerializer
    queryset = ContactFormModel.objects.all()
    


class ViewCalender(APIView):
    permission_classes = (IsStudent, )
    
    def get(self, request, *args, **kwargs):
    #student can view the calender of their courses
        student = self.request.user
        Class = self.kwargs['class_id']
        course = self.kwargs['course_id']
        if is_enrolled_in_course_and_class(student,Class,course):
            data = CalenderModel.objects.filter(
                    course = course, classes = Class
                )
            serializer = calenderSerializer(data, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(
                    {'message':'You are not enrolled in this course'}, 
                    status=HTTP_400_BAD_REQUEST
                    )

class CalenderDetail(APIView):
    permission_classes = (IsStudent, )

    def get_object(self,slug):
        try:
            return CalenderModel.objects.get(slug=slug)
        except:
            raise Http404

    def get(self,request,slug,format=None):
        #student can see the calender detail of their enrolled courses
        data = self.get_object(slug)
        course = data.course.id
        Class = data.classes.id
        student = self.request.user
        if is_enrolled_in_course_and_class(student,Class,course):
            serializer = calenderSerializer(data)
            return Response(serializer.data)
        else:
            return Response(
                {'message':'You are not enrolled in this course'}, 
                status=HTTP_400_BAD_REQUEST
                )


class ViewResults(APIView):
    #student can view the results of their enrolled courses (#obj perm)
    permission_classes = (IsStudent, )
    
    def get(self, request, *args, **kwargs):
        student = self.request.user
        Class = self.kwargs['class_id']
        course = self.kwargs['course_id']
        if is_enrolled_in_course_and_class(student,Class,course):
            data = ResultModel.objects.filter(
                    course = course, Class = Class, student__student=student
                )
            serializer = resultSerializer(data, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(
                    {'message':'You are not enrolled in this course'}, 
                    status=HTTP_400_BAD_REQUEST
                    )


class DetailResultView(APIView):
    permission_classes = (IsStudent, )

    def get_object(self,pk):
        try:
            return ResultModel.objects.get(id=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        #student can view the detail of results of their assigned courses (#obj perm)
        data = self.get_object(pk)
        course = data.course.id
        Class = data.Class.id
        student = self.request.user
        if is_enrolled_in_course_and_class(student,Class,course):
            if data.student.student == student:
                serializer = resultSerializer(data)
                return Response(serializer.data)
        return Response(
            {'message':'You are not enrolled in this course'}, 
            status=HTTP_400_BAD_REQUEST
            )
class StudentProfileView(APIView):
    permission_classes = (IsStudent, )

    def get_object(self,user):
        try:
            return StudentModel.objects.get(student = user)
        except:
            raise Http404 

    def get(self, request, *args, **kwargs):
        user = get_user_from_token(request)
        student = self.get_object(user)
        serializer = StudentProfileSerializer(student)
        return Response(serializer.data)



class ViewTest(generics.ListAPIView):
    '''Student can see the Tests of those courses and classess in which he/she is enrolled'''
    permission_classes = (IsStudent, )
    serializer_class = testSerializer
    
    def get(self, request, *args, **kwargs):
        student = request.user.id
        course_id = self.kwargs['course_id']
        class_id = self.kwargs["class_id"]
        #if student is enrolled in a class/course
        is_enrolled = is_enrolled_in_course_and_class(student,class_id,course_id)
        if is_enrolled == True:
            return self.list(request, *args, **kwargs)
        else:
            return Response(
                {'message':'You are not enrolled in this course or class'}, 
                status=HTTP_400_BAD_REQUEST
                )

    def get_queryset(self):
        return testModel.objects.filter(
            course=self.kwargs['course_id'],
            Class=self.kwargs['class_id']
            )


class ViewTest(generics.ListAPIView):
    '''Student can see the Tests of those courses and classess in which he/she is enrolled'''
    permission_classes = (IsStudent, )
    serializer_class = testSerializer
    
    def get(self, request, *args, **kwargs):
        student = request.user.id
        course_id = self.kwargs['course_id']
        class_id = self.kwargs["class_id"]
        #if student is enrolled in a class/course
        is_enrolled = is_enrolled_in_course_and_class(student,class_id,course_id)
        if is_enrolled == True:
            return self.list(request, *args, **kwargs)
        else:
            return Response(
                {'message':'You are not enrolled in this course or class'}, 
                status=HTTP_400_BAD_REQUEST
                )

    def get_queryset(self):
        return testModel.objects.filter(
            course=self.kwargs['course_id'],
            Class=self.kwargs['class_id']
            )


class ViewNotes(generics.ListAPIView):
    permission_classes = (IsStudent, )
    serializer_class = NotesSerializer
    
    def get(self, request, *args, **kwargs):
        student = request.user.id
        teacher_id = self.kwargs['teacher_id']
        is_enrolled = is_enrolled_with_teacher(student,teacher_id)
        if is_enrolled == True:
            return self.list(request, *args, **kwargs)
        else:
            return Response(
                {'message':'You are not enrolled with this teacher'}, 
                status=HTTP_400_BAD_REQUEST
                )

    def get_queryset(self):
        return NotesModel.objects.filter(
            teacher=self.kwargs['teacher_id']
            )



class Submittest(generics.ListCreateAPIView):
    ''' if student is enrolled in a course and class whose test is assigned then he/she can submit th test'''
    permission_classes = (IsStudent, )
    serializer_class = submittedtestSerializer

    def get_queryset(self):
        return SubmittestModel.objects.filter(
            test=self.kwargs['test_id'],
            student__student=self.request.user.id
            )

    def get_student_instance(self):
        student = StudentModel.objects.get(student=self.request.user.id)
        return student
        
    def perform_create(self, serializer):
        test = testModel.objects.get(id=self.kwargs['test_id'])
        student = self.request.user.id
        class_id = test.teacher.classes.id
        course_id = test.teacher.course.id
        #check student is enrolled in class/course or not.
        is_enrolled = is_enrolled_in_course_and_class(student,class_id,course_id)
        if is_enrolled == True:
            #if student have already submitted the test
            submit_test = SubmittestModel.objects.filter(
                student__student=student, test=test
                )
            if submit_test.exists():
                if submit_test[0].is_submit:
                    raise PermissionDenied('You have already submitted the test') 
            else:
                serializer.save(
                    student=self.get_student_instance(),
                    test=test, is_submit=True
                )
        elif is_enrolled == False:
            raise PermissionDenied('You cannot submit the test because you are not enrolled in this course') 


class ViewQuestion(generics.ListAPIView):
    '''Student can see the Tests of those courses and classess in which he/she is enrolled'''
    permission_classes = (IsStudent, )
    serializer_class = questionSerializer
    
    def get(self, request, *args, **kwargs):
        student = request.user.id
        course_id = self.kwargs['course_id']
        class_id = self.kwargs["class_id"]
        #if student is enrolled in a class/course
        is_enrolled = is_enrolled_in_course_and_class(student,class_id,course_id)
        if is_enrolled == True:
            return self.list(request, *args, **kwargs)
        else:
            return Response(
                {'message':'You are not enrolled in this course or class'}, 
                status=HTTP_400_BAD_REQUEST
                )

    def get_queryset(self):
        return quizQuestionsAndAnswersModel.objects.filter(
            course=self.kwargs['course_id'],
            Class=self.kwargs['class_id']
            )



class Submitquestion(generics.ListCreateAPIView):
    ''' if student is enrolled in a course and class whose question is assigned then he/she can submit th question'''
    permission_classes = (IsStudent, )
    serializer_class = submittedquestionSerializer

    def get_queryset(self):
        return SubmitquestionModel.objects.filter(
            question=self.kwargs['question_id'],
            student__student=self.request.user.id
            )

    def get_student_instance(self):
        student = StudentModel.objects.get(student=self.request.user.id)
        return student
        
    def perform_create(self, serializer):
        question = quizQuestionsAndAnswersModel.objects.get(id=self.kwargs['question_id'])
        student = self.request.user.id
        class_id = question.teacher.classes.id
        course_id = question.teacher.course.id
        #check student is enrolled in class/course or not.
        is_enrolled = is_enrolled_in_course_and_class(student,class_id,course_id)
        if is_enrolled == True:
            #if student have already submitted the question
            submit_question = SubmitquestionModel.objects.filter(
                student__student=student, question=question
                )
            if submit_question.exists():
                if submit_question[0].is_submit:
                    raise PermissionDenied('You have already submitted the question') 
            else:
                serializer.save(
                    student=self.get_student_instance(),
                    question=question, is_submit=True
                )
        elif is_enrolled == False:
            raise PermissionDenied('You cannot submit the question because you are not enrolled in this course') 

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

class ViewAttendance(APIView):
    #student can view the Attendance of their enrolled courses (#obj perm)
    permission_classes = (IsStudent, )
    
    def get(self, request, *args, **kwargs):
        student = self.request.user
        Class = self.kwargs['class_id']
        course = self.kwargs['course_id']
        if is_enrolled_in_course_and_class(student,Class,course):
            data = StudentAttendanceModel.objects.filter(
                    course = course, Class = Class, student__student=student
                )
            serializer = StudentAttendanceSerializer(data, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(
                    {'message':'You are not enrolled in this course'}, 
                    status=HTTP_400_BAD_REQUEST
                    )
class DetailAttendanceView(APIView):
    permission_classes = (IsStudent, )

    def get_object(self,pk):
        try:
            return StudentAttendanceModel.objects.get(id=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        #student can view the detail of attendance of their assigned courses (#obj perm)
        data = self.get_object(pk)
        course = data.course.id
        Class = data.Class.id
        student = self.request.user
        if is_enrolled_in_course_and_class(student,Class,course):
            if data.student.student == student:
                serializer = StudentAttendanceSerializer(data)
                return Response(serializer.data)
        return Response(
            {'message':'You are not enrolled in this course'}, 
            status=HTTP_400_BAD_REQUEST
            )
class ViewAnnoucement(APIView):
    #student can view the Annoucement of their enrolled courses (#obj perm)
    permission_classes = (IsStudent, )
    
    def get(self, request, *args, **kwargs):
        student = self.request.user.id
        Class = self.kwargs['class_id']
        course = self.kwargs['course_id']
        if is_enrolled_in_course_and_class(student,Class,course):
            data = TeacherAnnouncementModel.objects.filter(
                    course = course, Class = Class,
                )
            serializer = TeacherAnnouncementSerializer(data, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(
                    {'message':'You are not enrolled in this course'}, 
                    status=HTTP_400_BAD_REQUEST
                    )
    """ permission_classes = (IsStudent, )
    serializer_class = TeacherAnnouncementSerializer
    def get(self, request, *args, **kwargs):
            #check student is enrolled in a course or class
            student = self.request.user.id
            class_id = self.kwargs['class_id']
            course_id = self.kwargs['course_id']
            is_enrolled = is_enrolled_in_course_and_class(student,class_id,course_id)
            if is_enrolled == True:
                return self.list(request, *args, **kwargs)
            else:
                return Response(
                    {'message':'You are not enrolled in this course or class'}, 
                    status=HTTP_400_BAD_REQUEST
                    )
    def get_queryset(self):
            return TeacherAnnouncementModel.objects.filter(
                course=self.kwargs['course_id'], 
                Class=self.kwargs['class_id']
            ) """
                
class DetailAnnouncementView(APIView):
    permission_classes = (IsStudent, )

    def get_object(self,pk):
        try:
            return TeacherAnnouncementModel.objects.get(id=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        #student can view the detail of announcement of their assigned courses (#obj perm)
        data = self.get_object(pk)
        course = data.course.id
        Class = data.Class.id
        student = self.request.user.id
        if is_enrolled_in_course_and_class(student,Class,course):
            serializer = TeacherAnnouncementSerializer(data)
            return Response(serializer.data)
        return Response(
            {'message':'You are not enrolled in this course'}, 
            status=HTTP_400_BAD_REQUEST
            )