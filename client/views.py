from django.shortcuts import render

# ***************** API ****************
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser,FormParser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets,permissions
from rest_framework import generics
# from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly, AllowAny
from django.contrib.auth import get_user_model
from rest_auth.registration.views import RegisterView
from client.models import ClientModel
from .serializers import *
from .permissions import IsClient
from superadmin.models import *
from superadmin.serializers import *
User = get_user_model()

def get_user_from_token(request):
    '''It will given the current username by using token'''
    token = request.user.auth_token
    user = User.objects.get(id=token.user_id)
    return user
    

def is_enrolled_in_course(client,course_id):
        enrolled_client_data = ClientModel.objects.filter(client__client = client)
        print(enrolled_client_data, course_id)
        if enrolled_client_data.exists():
            enrolled_courses_id = []
            for enrolled_client in enrolled_client_data:
                enrolled_courses_id.append(enrolled_client.course.id)
            if course_id in enrolled_courses_id:
                return True
            else:
                return False
        else:
            return False

class ViewAndSubmitFeedback(generics.ListCreateAPIView):
    permission_classes = (IsClient, )
    serializer_class = ClientFeedbackSerializer

    def get_queryset(self):
        return ClientFeedBackModel.objects.filter(
            course=self.kwargs['course_id'],
            client__client= self.request.user.id
            )

    def get_client_instance(self):
        client = ClientModel.objects.get(client=self.request.user.id)
        return client

    def get_course_instance(self):
        course = CourseModel.objects.get(id=self.kwargs['course_id'])
        return course

    
    def perform_create(self, serializer):
        #check client is enrolled in a course or not
        client = self.request.user.id
        course_id = self.kwargs['course_id']
        is_enrolled = is_enrolled_in_course(client,course_id)
        if is_enrolled == True:
            serializer.save(
                client=self.get_client_instance(),
                course=self.get_course_instance(), 
                )
        else:
            raise PermissionDenied('You are not enrolled in this course ')


class SubmitComplain(generics.CreateAPIView):
    permission_classes = (IsClient, )
    serializer_class = submitComplainSerializer
    queryset = SubmitClientComplainModel.objects.all()



class ClientRegistrationView(RegisterView):
    serializer_class = ClientRegistrationSerializer
    permission_classes = (AllowAny,)


class ClientProfileView(APIView):
    permission_classes = (IsClient, )

    def get_object(self,user):
        try:
            return ClientModel.objects.get(client = user)
        except:
            raise Http404 

    def get(self, request, *args, **kwargs):
        user = get_user_from_token(request)
        client = self.get_object(user)
        serializer = ClientProfileSerializer(client)
        return Response(serializer.data)


class View_Annnouncement(generics.ListAPIView):
    permission_classes = (IsClient, )
    serializer_class = AnnouncementSerializer
    queryset = AnnouncementModel.objects.all()


class DetailView_Announcement(generics.RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (IsClient, )
    serializer_class = AnnouncementSerializer
    queryset = AnnouncementModel.objects.all()

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


class Enroll_CourseView(APIView):
    #student can view the results of their enrolled courses (#obj perm)
    permission_classes = (IsClient, )
    
    def get(self, request, *args, **kwargs):
        client = self.request.user
        course = self.kwargs['course_id']
        if is_enrolled_in_course(client,course):
            data = Enroll_CourseModel.objects.filter(
                    course = course, client__client=client
                )
            serializer = EnrollCourseSerializer(data, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(
                    {'message':'You are not enrolled in this course'}, 
                    status=HTTP_400_BAD_REQUEST
                    )

class DetailCourse_EnrollView(APIView):
    permission_classes = (IsClient, )

    def get_object(self,pk):
        try:
            return Enroll_CourseModel.objects.get(id=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        #client can view the detail of their enroll courses (#obj perm)
        data = self.get_object(pk)
        course = data.course.id
        client = self.request.user
        if is_enrolled_in_course(client,course):
            if data.client.client == client:
                serializer = ViewEnrollCourseSerializer(data)
                return Response(serializer.data)
        return Response(
            {'message':'You are not enrolled in this course'}, 
            status=status.HTTP_400_BAD_REQUEST
            )                    