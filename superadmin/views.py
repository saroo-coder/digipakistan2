import imp
from django.shortcuts import render

# ***************** API ****************
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser,FormParser
from .models import *
from django.http import Http404
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets,permissions
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from client.models import ClientModel
from adminapp.models import SchoolModel
from adminapp.serializers import SchoolSerializer

from .custompermissions import *
from client.permissions import *
from rest_framework.authentication import SessionAuthentication
from Student.permissions import IsStudent

User = get_user_model()

def get_user_from_token(request):
	token = request.user.auth_token #auth key(token) of current user 91391f4c12b94b753d08008150d2315d9d8d7e1e
	print("token.user_id",token.user_id) #gives id of user (pk)  2
	user = User.objects.get(id=token.user_id) #gives user name
	return user

# Create your views here.

# class UserListView(generics.ListAPIView):
#     parser_classes = (MultiPartParser,FormParser)
#     queryset = UserModel.objects.all()
#     serializer_class = UserSerializer

# class UserDetailView(generics.RetrieveAPIView):
#     parser_classes = (MultiPartParser,FormParser)
#     queryset = UserModel.objects.all()
#     serializer_class = UserSerializer

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


class ArticleDeleteUpdate(generics.RetrieveUpdateDestroyAPIView):
    '''
    Get: superadmin can see all articles (draft, published)
    PATCH : superadmin can mark article as published by changing status = P
    Delete: superadmin can delete article.
    '''
    lookup_field = 'slug'
    permission_classes = (IsSuperUser, )
    serializer_class = UpdateArticleSerializer
    queryset = ArticleModel.objects.all()


class AddQuestions(generics.CreateAPIView):
    permission_classes = (IsSuperUser, )
    serializer_class = QuestionSerializer
    queryset = QuestionModel.objects.all()

class ViewQuestion(generics.ListAPIView):
    permission_classes = (IsClient, )
    serializer_class = QuestionSerializer
    queryset = QuestionModel.objects.all()


class QuestionDetailView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (IsClient, )
    serializer_class = QuestionSerializer
    queryset = QuestionModel.objects.all()

class QuestionDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    permission_classes = (IsSuperUser, )
    serializer_class = QuestionSerializer
    queryset = QuestionModel.objects.all()


class AddSchools(generics.CreateAPIView):
    permission_classes = (IsSuperUser, )
    serializer_class = SchoolSerializer
    queryset = SchoolModel.objects.all()

class ViewSchool(generics.ListAPIView):
    permission_classes = (IsClient, )
    serializer_class = SchoolSerializer
    queryset = SchoolModel.objects.all()


class SchoolDetailView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (IsClient, )
    serializer_class = SchoolSerializer
    queryset = SchoolModel.objects.all()

class SchoolDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    permission_classes = (IsSuperUser, )
    serializer_class = SchoolSerializer
    queryset = SchoolModel.objects.all()


class AddBlogs(generics.CreateAPIView):
    permission_classes = (IsSuperUser, )
    serializer_class = BlogSerializer
    queryset = BlogModel.objects.all()

class ViewBlog(generics.ListAPIView):
    permission_classes = (IsClient, )
    serializer_class = BlogSerializer
    queryset = BlogModel.objects.all()


class BlogDetailView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (IsClient, )
    serializer_class = BlogSerializer
    queryset = BlogModel.objects.all()

class BlogDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    permission_classes = (IsSuperUser, )
    serializer_class = BlogSerializer
    queryset = BlogModel.objects.all()


class AddEventView(generics.CreateAPIView):
    #only super user can add events
    permission_classes = (IsSuperUser, )
    serializer_class = EventSerializer
    queryset = EventModel.objects.all()


class ListEventView(generics.ListAPIView):
    #Anyone can see the events
    permission_classes = (AllowAny, )
    serializer_class = EventSerializer
    queryset = EventModel.objects.all()


class EventDetailView(generics.RetrieveAPIView):
    #Anyone can see the detail of events
    lookup_field = 'slug'
    permission_classes = (AllowAny, )
    serializer_class = EventSerializer
    queryset = EventModel.objects.all()

class EventDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    #only superadmin can delete and update events
    lookup_field = 'slug'
    permission_classes = (IsSuperUser, )
    serializer_class = EventSerializer
    queryset = EventModel.objects.all()

class AddBusinessPartners(generics.CreateAPIView):
    permission_classes = (IsSuperUser, )
    serializer_class = BusinessPartnersSerializer
    queryset = BusinessPartnersModel.objects.all()

class ViewBusinessPartner(generics.ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = BusinessPartnersSerializer
    queryset = BusinessPartnersModel.objects.all()


class BusinessPartnerDetailView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (AllowAny, )
    serializer_class = BusinessPartnersSerializer
    queryset = BusinessPartnersModel.objects.all()

class BusinessPartnerDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    permission_classes = (IsSuperUser, )
    serializer_class = BusinessPartnersSerializer
    queryset = BusinessPartnersModel.objects.all()

class AddKidStory(generics.CreateAPIView):
    #Students can add kidstory
    permission_classes = (IsStudent, )
    serializer_class = KidStorySerializer
    queryset = KidStoryModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ViewKidStory(generics.ListAPIView):
    # anyone can see published kids story
    permission_classes = (AllowAny, )
    serializer_class = KidStorySerializer
    queryset = KidStoryModel.objects.filter(status__exact="P")


class KidStoryDetailView(generics.RetrieveAPIView):
    #anyone can see detail of published kids story
    lookup_field = 'slug'
    permission_classes = (AllowAny, )
    serializer_class = KidStorySerializer
    queryset = KidStoryModel.objects.filter(status__exact="P")

class KidStoryDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    '''
    Get: superadmin can see all stories (draft, published)
    PATCH : superadmin can mark stories as published by changing status = P
    Delete: superadmin can delete stories.
    '''
    lookup_field = 'slug'
    permission_classes = (IsSuperUser, )
    serializer_class = UpdateKidsStorySerializer
    queryset = KidStoryModel.objects.all()


class AddKidTalent(generics.CreateAPIView):
    #Students or client can add KidsTalent
    permission_classes = (IsStudentORClient, )
    serializer_class = KidTalentSerializer
    queryset = KidTalentModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ViewKidTalent(generics.ListAPIView):
    # anyone can see published kids talent
    permission_classes = (AllowAny, )
    serializer_class = KidTalentSerializer
    queryset = KidTalentModel.objects.filter(status__exact="P")


class KidTalentDetailView(generics.RetrieveAPIView):
    #anyone can see detail of published kids talent
    lookup_field = 'slug'
    permission_classes = (AllowAny, )
    serializer_class = KidTalentSerializer
    queryset = KidTalentModel.objects.filter(status__exact="P")

class KidTalentDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    '''
    Get: superadmin can see all kids talent (draft, published)
    PATCH : superadmin can mark kids talent as published by changing status = P
    Delete: superadmin can delete kids talent.
    '''
    lookup_field = 'slug'
    permission_classes = (IsSuperUser, )
    serializer_class = UpdateKidsTalentSerializer
    queryset = KidTalentModel.objects.all()


class AddCourses(generics.CreateAPIView):
    permission_classes = (IsSuperUser, )
    serializer_class = CourseSerializer
    queryset = CourseModel.objects.all()

class ViewCourse(generics.ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = CourseSerializer
    queryset = CourseModel.objects.all()


class CourseDetailView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (AllowAny, )
    serializer_class = CourseSerializer
    queryset = CourseModel.objects.all()

class CourseDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    permission_classes = (IsSuperUser, )
    serializer_class = CourseSerializer
    queryset = CourseModel.objects.all()


class AddQuizContext(generics.CreateAPIView):
    permission_classes = (IsSuperUser, )
    serializer_class = QuizContextSerializer
    queryset = QuizContextModel.objects.all()

class ViewQuizContext(generics.ListAPIView):
    permission_classes = (IsClient, )
    serializer_class = QuizContextSerializer
    queryset = QuizContextModel.objects.all()


class QuizContextDetailView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (IsClient, )
    serializer_class = QuizContextSerializer
    queryset = QuizContextModel.objects.all()

class QuizContextDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    permission_classes = (IsSuperUser, )
    serializer_class = QuizContextSerializer
    queryset = QuizContextModel.objects.all()


class AddFeedback(generics.CreateAPIView):
    permission_classes = (IsSuperUser, )
    serializer_class = ClientFeedbackSerializer
    queryset = ClientFeedBackModel.objects.all()

class ViewFeedback(generics.ListAPIView):
    permission_classes = (IsClient, )
    serializer_class = ClientFeedbackSerializer
    queryset = ClientFeedBackModel.objects.all()


class FeedbackDetailView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (IsClient, )
    serializer_class = ClientFeedbackSerializer
    queryset = ClientFeedBackModel.objects.all()

class FeedbackDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    permission_classes = (IsSuperUser, )
    serializer_class = ClientFeedbackSerializer
    queryset = ClientFeedBackModel.objects.all()


class AddWebsiteAd(generics.CreateAPIView):
    permission_classes = (IsSuperUser, )
    serializer_class = WebsiteAdSerializer
    queryset = WebsiteAdModel.objects.all()

class ViewWebsiteAd(generics.ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = WebsiteAdSerializer
    queryset = WebsiteAdModel.objects.all()


class WebsiteAdDetailView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (AllowAny, )
    serializer_class = WebsiteAdSerializer
    queryset = WebsiteAdModel.objects.all()

class WebsiteAdDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    permission_classes = (IsSuperUser, )
    serializer_class = WebsiteAdSerializer
    queryset = WebsiteAdModel.objects.all()





# class AddApproval(generics.CreateAPIView):
#     permission_classes = (IsSuperUser, )
#     serializer_class = ApprovalSerializer
#     queryset = ApprovalModel.objects.all()

# class ViewApproval(generics.ListAPIView):
#     permission_classes = (IsClient, )
#     serializer_class = ApprovalSerializer
#     queryset = ApprovalModel.objects.all()


# class ApprovalDetailView(generics.RetrieveAPIView):
#     lookup_field = 'slug'
#     permission_classes = (IsClient, )
#     serializer_class = ApprovalSerializer
#     queryset = ApprovalModel.objects.all()

# class ApprovalDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
#     lookup_field = 'slug'
#     permission_classes = (IsSuperUser, )
#     serializer_class = ApprovalSerializer
#     queryset = ApprovalModel.objects.all()


class AddBusinessPromotion(generics.CreateAPIView):
    permission_classes = (IsSuperUser, )
    serializer_class = BusinessPromotionSerializer
    queryset = BusinessPromotionModel.objects.all()

class ViewBusinessPromotion(generics.ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = BusinessPromotionSerializer
    queryset = BusinessPromotionModel.objects.all()


class BusinessPromotionDetailView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (AllowAny, )
    serializer_class = BusinessPromotionSerializer
    queryset = BusinessPromotionModel.objects.all()

class BusinessPromotionDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    permission_classes = (IsSuperUser, )
    serializer_class = BusinessPromotionSerializer
    queryset = BusinessPromotionModel.objects.all()


class AddTeam(generics.CreateAPIView):
    permission_classes = (IsSuperUser, )
    serializer_class = TeamSerializer
    queryset = TeamModel.objects.all()

class ViewTeam(generics.ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = TeamSerializer
    queryset = TeamModel.objects.all()


class TeamDetailView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (AllowAny, )
    serializer_class = TeamSerializer
    queryset = TeamModel.objects.all()

class TeamDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    permission_classes = (IsSuperUser, )
    serializer_class = TeamSerializer
    queryset = TeamModel.objects.all()


class AddAdvisoryBoard(generics.CreateAPIView):
    permission_classes = (IsSuperUser, )
    serializer_class = AdvisoryBoardSerializer
    queryset = AdvisoryBoardModel.objects.all()

class ViewAdvisoryBoard(generics.ListAPIView):
    permission_classes = (IsSuperUser, )
    serializer_class = AdvisoryBoardSerializer
    queryset = AdvisoryBoardModel.objects.all()


class AdvisoryBoardDetailView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (IsSuperUser, )
    serializer_class = AdvisoryBoardSerializer
    queryset = AdvisoryBoardModel.objects.all()

class AdvisoryBoardDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    permission_classes = (IsSuperUser, )
    serializer_class = AdvisoryBoardSerializer
    queryset = AdvisoryBoardModel.objects.all()



class AddAnnouncement(generics.CreateAPIView):
    permission_classes = (IsSuperUser, )
    serializer_class = AnnouncementSerializer
    queryset = AnnouncementModel.objects.all()


class ListAnnouncement(generics.ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = AnnouncementSerializer
    queryset = AnnouncementModel.objects.all()


class AnnouncementDetail(generics.RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (AllowAny, )
    serializer_class = AnnouncementSerializer
    queryset = AnnouncementModel.objects.all()

class AnnouncementDeleteUpdate(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    permission_classes = (IsSuperUser, )
    serializer_class = AnnouncementSerializer
    queryset = AnnouncementModel.objects.all()


class SuperadminProfileView(APIView):
    permission_classes = (IsSuperUser, )

    def get(self, request, *args, **kwargs):
        user = get_user_from_token(request)
        data = {
            'name': user.username,
            'email': user.email
        }
        return Response(data)



class AddJobClassified(generics.CreateAPIView):
    permission_classes = (IsSuperUser, )
    serializer_class = JobClassifiedSerializer
    queryset = JobClassifiedModel.objects.all()

class ViewJobClassified(generics.ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = JobClassifiedSerializer
    queryset = JobClassifiedModel.objects.all()


class JobClassifiedDetailView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (AllowAny, )
    serializer_class = JobClassifiedSerializer
    queryset = JobClassifiedModel.objects.all()

class JobClassifiedDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    permission_classes = (IsSuperUser, )
    serializer_class = JobClassifiedSerializer
    queryset = JobClassifiedModel.objects.all()



class AddCustomerReviews(generics.CreateAPIView):
    permission_classes = (IsSuperUser, )
    serializer_class = CustomerReviewSerializer
    queryset = CustomerReviewModel.objects.all()

class ViewCustomerReview(generics.ListAPIView):
    permission_classes = (IsClient, )
    serializer_class = CustomerReviewSerializer
    queryset = CustomerReviewModel.objects.all()


class CustomerReviewDetailView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (IsClient, )
    serializer_class = CustomerReviewSerializer
    queryset = CustomerReviewModel.objects.all()

class CustomerReviewDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    permission_classes = (IsSuperUser, )
    serializer_class = CustomerReviewSerializer
    queryset = CustomerReviewModel.objects.all()



class ClientComplain(APIView):

    permission_classes = (IsSuperUser, )
    serializer = ViewComplainSerializer(many=True)


class clientfeedback(APIView):

    permission_classes = (IsSuperUser, )

    def get(self, request, format=None):
        feeds = ClientFeedBackModel.objects.filter(
            Class__admin = self.request.user
        )
        serializer = ClientFeedbackSerializer(feeds, many=True)
        return Response(serializer.data)

class Enroll_Course(APIView):
    permission_classes = (IsSuperUser, )
    def post(self, request, format=None):
        serializer = EnrollCourseSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            course = serializer.validated_data.get('course', '')
            serializer.save()
            return Response(serializer.data,status =status.HTTP_201_CREATED)
            
        else:
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)
class ViewEnroll_Course(APIView):
    permission_classes = (IsSuperUser, )
    
    def get(self, request, *args, **kwargs):
        course = self.kwargs['course_id']
        client = self.kwargs['client_id']
        data = Enroll_CourseModel.objects.filter(
                    course = course, client = client
                )
        serializer = ViewEnrollCourseSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DetailEnroll_CourseView(APIView):
    permission_classes = (IsSuperUser, )

    def get_object(self,pk):
        try:
            return Enroll_CourseModel.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = ViewEnrollCourseSerializer(data)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        data = self.get_object(pk)
        serializer = ViewEnrollCourseSerializer(data,data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

    def delete(self,request,pk,format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        
                
class CourseDetail(APIView):
    permission_classes = (IsSuperUser, )

    def get_object(self, slug):
        try:
            return CourseModel.objects.get(slug=slug)
        except CourseModel.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        data = self.get_object(slug)
        if data.classes.school.admin == self.request.user:
            serializer = ViewCourseSerializer(data)
            return Response(serializer.data)
        else:
            return Response(
                {'message':'This course does not belong to your school'}, 
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self,request,slug,format=None):
        data = self.get_object(slug)
        if data.course.client.admin == self.request.user:
            serializer = CourseSerializer(data,data = request.data)
            if serializer.is_valid(raise_exception=True):
                course = serializer.validated_data.get('course', '')
                if course.client.admin == self.request.user:
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
                return Response(
                    {'message':'This Class does not belong to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
             return Response(
                    {'message':'This course does not belong to you'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )

    def delete(self,request,slug,format=None):
        data = self.get_object(slug)
        if data.course.client.admin == self.request.user:
            data.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {'message':'This course does not belong to you'}, 
                status=status.HTTP_400_BAD_REQUEST
                )

class SchoolRegistrationView(RegisterView):
    serializer_class = RegisterSchoolSerializer
    permission_classes = (IsSuperUser,)
              
class Add_question(generics.CreateAPIView):
    permission_classes = (IsSuperUser, )
    def post(self,request,format=None):
        serializer = QuestionSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            course = serializer.validated_data.get('course', '')
            serializer.save()
            return Response(serializer.data,status =status.HTTP_201_CREATED)
            
        else:
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)

class Viewquestion(generics.ListAPIView):
    permission_classes = (IsSuperUser, )
    
    def get(self, request, *args, **kwargs):
        course = self.kwargs['course_id']
        data = QuestionModel.objects.filter(
                    course_id = course)
        serializer = QuestionSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class QuestionDetail(APIView):
    permission_classes = (IsSuperUser, )

    def get_object(self,pk):
        try:
            return QuestionModel.objects.get(id=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        data = self.get_object(pk)
        serializer = QuestionSerializer(data)
        return Response(serializer.data)
    

    def put(self,request,pk,format=None):
       data = self.get_object(pk)
       serializer = QuestionSerializer(data,data = request.data)
       if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
    def delete(self,request,pk,format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
class SubmittedQuestionView(APIView):
    permission_classes = (IsSuperUser, )
    
    def get(self, request, *args, **kwargs):
        admin = self.request.user
        course = self.kwargs['course_id']
        client = self.kwargs['client_id']
        data = Client_SubmitquestionModel.objects.filter(
                course__course = course,
                client__client = client
            )
        serializer = Client_submittedquestionSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)   

class AddonlineTest(generics.CreateAPIView):
    permission_classes = (IsSuperUser, )
    def post(self, request, format=None):
        serializer = testSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            course = serializer.validated_data.get('course', '')
            serializer.save()
            return Response(serializer.data,status =status.HTTP_201_CREATED)
            
        else:
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)

class ViewOnlinetest(generics.ListAPIView):
    permission_classes = (IsSuperUser, )
    
    def get(self, request, *args, **kwargs):
        course = self.kwargs['course_id']
        data = Client_testModel.objects.filter(
                    course_id = course)
        serializer = testSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class onlinetestDetail(APIView):
    permission_classes = (IsSuperUser, )

    def get_object(self,pk):
        try:
            return Client_testModel.objects.get(id=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        data = self.get_object(pk)
        serializer = testSerializer(data)
        return Response(serializer.data)
    

    def put(self,request,pk,format=None):
       data = self.get_object(pk)
       serializer = testSerializer(data,data = request.data)
       if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
    def delete(self,request,pk,format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)            

class SubmittedonlineTestView(APIView):
    permission_classes = (IsSuperUser, )
    
    def get(self, request, *args, **kwargs):
        admin = self.request.user
        course = self.kwargs['course_id']
        client = self.kwargs['client_id']
        data = Client_SubmittestModel.objects.filter(
                course__course = course,
                client__client = client
            )
        serializer = Client_submittedtestSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)