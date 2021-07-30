from parentApp.permissions import IsParent
from django.shortcuts import render
from superadmin.models import *
from superadmin.serializers import  *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets,permissions
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser,FormParser
from rest_framework import generics
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from adminapp.models import *
from adminapp.serializers import  *
from Student.models import *
from Student.serializers import  *
from teacherApp.models import *
from teacherApp.serializers import  *



# Create your views here.

def is_enrolled_in_course_and_class(parent,class_id,course_id):
        #check parent is enrolled in given class or course.
        enrolled_parent_data = Enroll_ParentModel.objects.filter(parent__parent = parent)
        print(enrolled_parent_data, class_id, course_id)
        if enrolled_parent_data.exists():
            enrolled_courses_id = []
            enrolled_classes_id = []
            for enrolled_parent in enrolled_parent_data:
                enrolled_courses_id.append(enrolled_parent.course.id)
                enrolled_classes_id.append(enrolled_parent.classes.id)
            if course_id in enrolled_courses_id and class_id in enrolled_classes_id:
                return True
            else:
                return False
        else:
            return False

class ViewAnnoucement(APIView):
    permission_classes = (IsParent, )
    
    def get(self, request, *args, **kwargs):
        parent = self.request.user.id
        Class = self.kwargs['class_id']
        course = self.kwargs['course_id']
        if is_enrolled_in_course_and_class(parent,Class,course):
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


class ViewAndSubmitFeedback(generics.ListCreateAPIView):
    permission_classes = (IsParent, )
    serializer_class = ParentFeedbackSerializer

    def get_queryset(self):
        return ParentFeedBackModel.objects.filter(
            course=self.kwargs['course_id'],
            Class=self.kwargs['class_id'],
            parent__parent= self.request.user.id
            )

    def get_parent_instance(self):
        parent = ParentModel.objects.get(parent=self.request.user.id)
        return parent

    def get_course_instance(self):
        course = CourseModel.objects.get(id=self.kwargs['course_id'])
        return course

    def get_class_instance(self):
        course = TblClassModel.objects.get(id=self.kwargs['class_id'])
        return course

    def perform_create(self, serializer):
        #check parent is enrolled in a course or not
        parent = self.request.user.id
        class_id = self.kwargs['class_id']
        course_id = self.kwargs['course_id']
        is_enrolled = is_enrolled_in_course_and_class(parent,class_id,course_id)
        if is_enrolled == True:
            serializer.save(
                parent=self.get_parent_instance(),
                course=self.get_course_instance(), 
                Class=self.get_class_instance()
                )
        else:
            raise PermissionDenied('You are not enrolled in this course or class')



class SubmitComplain(generics.CreateAPIView):
    permission_classes = (IsParent,)
    serializer_class = ComplainSerializer

    def perform_create(self, serializer):
        serializer.save(student=ViewAndSubmitFeedback.get_student_instance(self))


class ViewComplain(generics.ListAPIView):
    permission_classes = (IsParent,)
    serializer_class = ComplainSerializer
    queryset = ContactFormModel.objects.all()
    

class ViewEnrolledCourses(generics.ListAPIView):
    '''Authenticated Student can see their enrolled courses'''
    permission_classes = (IsParent, )
    serializer_class = ViewEnrollParentSerializer

    def get_queryset(self):
        return Enroll_ParentModel.objects.filter(parent__parent=self.request.user.id)
