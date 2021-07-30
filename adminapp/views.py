
from django.shortcuts import render
from adminapp.models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import Http404
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from rest_auth.registration.views import RegisterView
from .permissions import IsAdmin
from client.permissions import IsClient
from django.contrib.auth import get_user_model
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser,FormParser
from teacherApp.models import StudentFeedBackModel
from teacherApp.serializers import StudentFeedbackSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from superadmin.models import ArticleModel
from superadmin.serializers import ArticleSerializer
User = get_user_model()

def get_user_from_token(request):
    '''It will given the current username by using token'''
    token = request.user.auth_token
    user = User.objects.get(id=token.user_id)
    return user

# class View_Teacher(APIView):
#     def get(self, request, format=None):
#         teacher = TeacherModel.objects.all()
#         serializer = ViewTeacherSerializer(teacher, many=True)
#         return Response(serializer.data)
##
# Create your views here.


# class Add_Teacher(APIView):

#     def post(self, request, format = None):
#         serializer = TeacherSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class Add_Student(APIView):
#     def post(self, request, format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Assign_Course(APIView):
    #only admin can make this request
    permission_classes = (IsAdmin, )
    def post(self, request, format=None):
        serializer = AssignCourseSerializer(data=request.data)
        if serializer.is_valid():
            teacher = serializer.validated_data.get('teacher', '')
            Class = serializer.validated_data.get('classes', '')
            course = serializer.validated_data.get('course', '')
            if teacher.school.admin != self.request.user:
                return Response(
                    {'message':'This Teacher is enrolled in your school'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
            elif Class.school.admin != self.request.user:
                return Response(
                    {'message':'This class is not part of your school'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
            elif course.classes.school.admin != self.request.user:
                return Response(
                    {'message':'This course is not part of your school'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Add_Course(APIView):
    permission_classes = (IsAdmin, )

    def post(self, request, format=None):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            Class = serializer.validated_data.get('classes', '')
            if Class.school.admin != self.request.user:
                return Response(
                    {'message':'This course is not part of your school'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class View_Course(APIView):
    permission_classes = (IsAdmin, )
    
    def get(self, request, format=None):
        data = CourseModel.objects.filter(
                classes__school__admin = self.request.user
                )
        serializer = ViewCourseSerializer(data, many=True)
        return Response(serializer.data)

class CourseDetail(APIView):
    permission_classes = (IsAdmin, )

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
                status=HTTP_400_BAD_REQUEST
                )

    def put(self,request,slug,format=None):
        data = self.get_object(slug)
        if data.classes.school.admin == self.request.user:
            serializer = CourseSerializer(data,data = request.data)
            if serializer.is_valid(raise_exception=True):
                Class = serializer.validated_data.get('classes', '')
                if Class.school.admin == self.request.user:
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
                return Response(
                    {'message':'This Class does not belong to your school'}, 
                    status=HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
             return Response(
                    {'message':'This course does not belong to your school'}, 
                    status=HTTP_400_BAD_REQUEST
                    )

    def delete(self,request,slug,format=None):
        data = self.get_object(slug)
        if data.classes.school.admin == self.request.user:
            data.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {'message':'This course does not belong to your school'}, 
                status=HTTP_400_BAD_REQUEST
                )


class Add_Class(APIView):
    permission_classes = (IsAdmin, )
    def post(self, request, format=None):
        serializer = TblClassSerializer(data=request.data)
        if serializer.is_valid():
            school = serializer.validated_data.get('school','')
            if school.admin != self.request.user:
                return Response(
                    {'message':'You are not the admin of this school'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class View_Class(APIView):
    permission_classes = (IsAdmin, )
    def get(self, request, format=None):
        data = TblClassModel.objects.filter(
                school__admin = self.request.user
                )
        serializer = TblClassSerializer(data, many=True)
        return Response(serializer.data)


class Class_Detail(APIView):
    permission_classes = (IsAdmin, )

    def get_object(self, slug):
        try:
            return TblClassModel.objects.get(slug=slug)
        except TblClassModel.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        data = self.get_object(slug)
        if data.school.admin == self.request.user:
            serializer = TblClassSerializer(data)
            return Response(serializer.data)
        else:
            return Response(
                {'message':'This Class does not belong to your school'}, 
                status=HTTP_400_BAD_REQUEST
                )

    def put(self,request,slug,format=None):
        data = self.get_object(slug)
        if data.school.admin == self.request.user:
            serializer = EditClassSerializer(data,data = request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {'message':'This Class does not belong to your school'}, 
                status=HTTP_400_BAD_REQUEST
                ) 

    def delete(self,request,slug,format=None):
        data = self.get_object(slug)
        if data.school.admin == self.request.user:
            data.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {'message':'This Class does not belong to your school'}, 
                status=HTTP_400_BAD_REQUEST
                )

        
   
class Unassign_Course(APIView):
    permission_classes = (IsAdmin, )

    def get_object(self,pk):
        try:
            return Assign_TeacherModel.objects.get(id=pk)
        except:
            raise Http404

    def delete(self, request,assign_course_id,format=None):
        data = self.get_object(assign_course_id)
        if data.teacher.school.admin == self.request.user:
            data.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {'message':'You dont have right to unassign this course'}, 
                status=status.HTTP_400_BAD_REQUEST
                )

class Enroll_Student(APIView):
    '''Only admin can enroll students'''
    permission_classes = (IsAdmin, )

    def post(self, request, format=None):
        serializer = EnrollStudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.validated_data.get('student', '')
            Class = serializer.validated_data.get('classes', '')
            course = serializer.validated_data.get('course', '')
            if student.school.admin != self.request.user:
                return Response(
                    {'message':'This student is not enrolled in your school'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
            elif Class.school.admin != self.request.user:
                return Response(
                    {'message':'This class is not part of your school'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
            elif course.classes.school.admin != self.request.user:
                return Response(
                    {'message':'This course is not part of your school'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class Modify_Teacher(APIView):
#     def get_object(self, slug):
#         try:
#             return TeacherModel.objects.get(slug=slug)
#         except TeacherModel.DoesNotExist:
#             raise Http404

#     def get(self, request, slug, format=None):
#         teachers = self.get_object(slug)
#         serializer = TeacherSerializer(teachers)
#         return Response(serializer.data)

#     def put(self,request,slug):
#         data = self.get_object(slug)
#         serializer = TeacherSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.update()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class Modify_Student(APIView):
#     def get_object(self, slug):
#         try:
#             return StudentModel.objects.get(slug=slug)
#         except StudentModel.DoesNotExist:
#             raise Http404

#     def get(self, request, slug, format=None):
#         students = self.get_object(slug)
#         serializer = StudentSerializer(students)
#         return Response(serializer.data)

#     def put(self,request,slug):
#         data = self.get_object(slug)
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class Delete_Teacher(APIView):
#     def get_object(self, slug):
#         try:
#             return TeacherModel.objects.get(slug=slug)
#         except TeacherModel.DoesNotExist:
#             raise Http404
#     def delete(self, request, slug, format=None):
#         teachers = self.get_object(slug)
#         teachers.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class Delete_Student(APIView):
#     def get_object(self, slug):
#         try:
#             return StudentModel.objects.get(slug=slug)
#         except StudentModel.DoesNotExist:
#             raise Http404
#     def delete(self, request, slug, format=None):
#         students = self.get_object(slug)
#         students.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class feedback(APIView):
    '''admin can see the feedback of their school's course and class'''

    permission_classes = (IsAdmin, )

    def get(self, request, format=None):
        feeds = StudentFeedBackModel.objects.filter(
            # course__classes__school__admin = self.request.user,
            Class__school__admin = self.request.user
        )
        serializer = StudentFeedbackSerializer(feeds, many=True)
        return Response(serializer.data)


class ViewRespondedQueries(APIView):
    permission_classes = (IsAdmin, )

    def get(self, request, format=None):
        datas = ContactFormModel.objects.filter(
            student__school__admin = self.request.user,
            response_submitted = True
        )
        serializer = ViewQuerySerializer(datas, many=True)
        return Response(serializer.data)

class ViewUnRespondedQueries(APIView):
    permission_classes = (IsAdmin, )

    def get(self, request, format=None):
        datas = ContactFormModel.objects.filter(
            student__school__admin = self.request.user,
            response_submitted = False
        )
        serializer = ViewQuerySerializer(datas, many=True)
        return Response(serializer.data)

class Respond_Queries(APIView):
    permission_classes = (IsAdmin, )

    def get_object(self, pk):
        try:
            return ContactFormModel.objects.get(pk=pk)
        except ContactFormModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        datas = self.get_object(pk)
        if datas.student.school.admin == self.request.user:
            serializer = ViewQuerySerializer(datas)
            return Response(serializer.data)
        else:
            return Response(
                {'message':'You cannot get this query'}, 
                status=status.HTTP_400_BAD_REQUEST
                )
            

    def put(self,request,pk, format=None):
        data = self.get_object(pk)
        if data.student.school.admin == self.request.user:
            serializer = ResponseSerializer(data, data = request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(response_submitted=True)
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {'message':'You cannot respond to this query'}, 
                status=status.HTTP_400_BAD_REQUEST
                )


class StudentRegistrationView(RegisterView):
    serializer_class = StudentRegisterationSerializer
    permission_classes = (IsAdmin,)


class TeacherRegistrationView(RegisterView):
    serializer_class = TeacherRegisterationSerializer
    permission_classes = (IsAdmin,)

class ViewTeacher(APIView):
    #admin can view the records of his own school teachers
    permission_classes = (IsAdmin, )

    def get(self, request, *args, **kwargs):
        data = TeacherModel.objects.filter(
            school__admin = self.request.user
        )
        serializer = ViewTeacherSerializer(data, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class TeacherDetail(APIView):
    permission_classes = (IsAdmin, )

    def get_object(self,teacher_id):
        try:
            return TeacherModel.objects.get(pk=teacher_id)
        except:
            raise Http404

    def get(self,request,teacher_id,format=None):
        #admin can see the teacher details of his own school
        data = self.get_object(teacher_id)
        if data.school.admin == self.request.user:
            serializer = ViewTeacherSerializer(data)
            return Response(serializer.data)
        else:
            return Response(
                {'message':'This teacher does not belong to your school'}, 
                status=HTTP_400_BAD_REQUEST
                )

    def put(self,request,teacher_id,format=None):
        #admin can update the teacher details of his own school
        data = self.get_object(teacher_id)
        if data.school.admin == self.request.user:
            serializer = ViewTeacherSerializer(data,data = request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {'message':'This teacher does not belong to your school'}, 
                status=HTTP_400_BAD_REQUEST
                )

    def delete(self,request,teacher_id,format=None):
        data = self.get_object(teacher_id)
        if data.school.admin == self.request.user:
            data.teacher.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {'message':'This teacher does not belong to your school'}, 
                status=HTTP_400_BAD_REQUEST
                )


class ViewStudent(APIView):
    #admin can view the records of his own school students
    permission_classes = (IsAdmin, )

    def get(self, request, *args, **kwargs):
        data = StudentModel.objects.filter(
            school__admin = self.request.user
        )
        serializer = ViewStudentSerializer(data, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class StudentDetail(APIView):
    permission_classes = (IsAdmin, )

    def get_object(self,student_id):
        try:
            return StudentModel.objects.get(pk=student_id)
        except:
            raise Http404

    def get(self,request,student_id,format=None):
        #admin can see the student details of his own school
        data = self.get_object(student_id)
        if data.school.admin == self.request.user:
            serializer = ViewStudentSerializer(data)
            return Response(serializer.data)
        else:
            return Response(
                {'message':'This Student does not belong to your school'}, 
                status=HTTP_400_BAD_REQUEST
                )

    def put(self,request,student_id,format=None):
        #admin can update the student details of his own school
        data = self.get_object(student_id)
        if data.school.admin == self.request.user:
            serializer = ViewStudentSerializer(data,data = request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {'message':'This student does not belong to your school'}, 
                status=HTTP_400_BAD_REQUEST
                )

    def delete(self,request,student_id,format=None):
        data = self.get_object(student_id)
        if data.school.admin == self.request.user:
            data.student.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {'message':'This student does not belong to your school'}, 
                status=HTTP_400_BAD_REQUEST
                )
                
class SchoolsView(APIView):
    #admin can view the records of his own school Schools
    permission_classes = (IsAdmin, )

    def get(self, request, *args, **kwargs):
        data = SchoolModel.objects.filter(
            admin = self.request.user
        )
        serializer = SchoolSerializer(data, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, format=None):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SchoolDetail(APIView):
    permission_classes = (IsAdmin, )

    def get_object(self,school_id):
        try:
            return SchoolModel.objects.get(pk=school_id)
        except:
            raise Http404

    def get(self,request,school_id,format=None):
        #admin can see the student details of his own school
        data = self.get_object(school_id)
        if data.admin == self.request.user:
            serializer = SchoolSerializer(data)
            return Response(serializer.data)
        else:
            return Response(
                {'message':'This Student does not belong to your school'}, 
                status=HTTP_400_BAD_REQUEST
                )

    def put(self,request,school_id,format=None):
        #admin can update the student details of his own school
        data = self.get_object(school_id)
        if data.admin == self.request.user:
            serializer = SchoolSerializer(data,data = request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {'message':'This student does not belong to your school'}, 
                status=HTTP_400_BAD_REQUEST
                )

    def delete(self,request,school_id,format=None):
        data = self.get_object(school_id)
        if data.admin == self.request.user:
            data.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {'message':'This student does not belong to your school'}, 
                status=HTTP_400_BAD_REQUEST
                )                


# class ComplaintView(APIView):
#     parser_classes = (MultiPartParser,FormParser)
#     def get(self,request,format = None):
#         data = ComplaintModel.objects.all()
#         # Student = self.kwargs['student_id']
#         # data = CalenderModel.objects.filter(
#         #             course = course, classes = Class
#         #         )
#         serializer = ComplaintSerializer (data, many = True)
#         return Response(serializer.data,status = status.HTTP_200_OK)

#     def post(self,request, format=None):
#         serializer = ComplaintSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

# class DetailComplaintView(APIView):
#     parser_classes = (MultiPartParser,FormParser)
#     def get_object(self, pk):
#         try:
#             return ComplaintModel.objects.get(id=pk)
#         except ComplaintModel.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         data = self.get_object(pk)
#         serializer = ComplaintSerializer(data)
#         return Response(serializer.data)

#     def put(self,request,pk):
#         data = self.get_object(pk)
#         serializer = ComplaintSerializer(data , data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         data = self.get_object(pk)
#         data.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
 
class Role(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        user = get_user_from_token(request)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class AdminProfileView(APIView):
    permission_classes = (IsAdmin, )

    def get_object(self,user):
        try:
            return SchoolModel.objects.get(admin = user)
        except:
            raise Http404 

    def get(self, request, *args, **kwargs):
        user = get_user_from_token(request)
        admin = self.get_object(user)
        serializer = AdminProfileSerializer(admin)
        return Response(serializer.data)

# **************** Memona Work **********************

class Add_Class(APIView):
    def post(self, request, format=None):
        serializer = TblClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class View_Class(APIView):
    def get(self, request, format=None):
        courses = TblClassModel.objects.all()
        serializer = TblClassSerializer(courses, many=True)
        return Response(serializer.data)

class Edit_Class(APIView):
    def get_object(self, slug):
        try:
            return TblClassModel.objects.get(slug=slug)
        except TblClassModel.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        classes = self.get_object(slug)
        serializer = TblClassSerializer(classes)
        return Response(serializer.data)

    def put(self,request,slug):
        data = self.get_object(slug)
        serializer = TblClassSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Delete_Class(APIView):
    def get_object(self, slug):
        try:
            return TblClassModel.objects.get(slug=slug)
        except TblClassModel.DoesNotExist:
            raise Http404
    def delete(self, request, slug, format=None):
        classes = self.get_object(slug)
        classes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Add_Section(APIView):
    def post(self, request, format=None):
        serializer = TblSectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class View_Section(APIView):
    def get(self, request, format=None):
        courses = TblSectionModel.objects.all()
        serializer = TblSectionSerializer(courses, many=True)
        return Response(serializer.data)

class Edit_Section(APIView):
    def get_object(self, slug):
        try:
            return TblSectionModel.objects.get(slug=slug)
        except TblSectionModel.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        classes = self.get_object(slug)
        serializer = TblSectionSerializer(classes)
        return Response(serializer.data)

    def put(self,request,slug):
        data = self.get_object(slug)
        serializer = TblSectionSerializer(instance=data,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Delete_Section(APIView):
    def get_object(self, slug):
        try:
            return TblSectionModel.objects.get(slug=slug)
        except TblSectionModel.DoesNotExist:
            raise Http404
    def delete(self, request, slug, format=None):
        classes = self.get_object(slug)
        classes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SchoolsView(APIView):
    #admin can view the records of his own school Schools
    permission_classes = (IsAdmin, )

    def get(self, request, *args, **kwargs):
        data = SchoolModel.objects.filter(
            admin = self.request.user
        )
        # data = SchoolModel.objects.all()
        serializer = SchoolSerializer(data, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, format=None):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SchoolDetail(APIView):
    permission_classes = (IsAdmin, )

    def get_object(self,school_id):
        try:
            return SchoolModel.objects.get(pk=school_id)
        except:
            raise Http404

    def get(self,request,school_id,format=None):
        #admin can see the student details of his own school
        data = self.get_object(school_id)
        if data.admin == self.request.user:
            serializer = SchoolSerializer(data)
            return Response(serializer.data)
        else:
            return Response(
                {'message':'This Student does not belong to your school'}, 
                status=HTTP_400_BAD_REQUEST
                )

    def put(self,request,school_id,format=None):
        #admin can update the student details of his own school
        data = self.get_object(school_id)
        if data.admin == self.request.user:
            serializer = SchoolSerializer(data,data = request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {'message':'This student does not belong to your school'}, 
                status=HTTP_400_BAD_REQUEST
                )

    def delete(self,request,school_id,format=None):
        data = self.get_object(school_id)
        if data.admin == self.request.user:
            data.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {'message':'This student does not belong to your school'}, 
                status=HTTP_400_BAD_REQUEST
                )                

# **************** Memona Work **********************


class AddAnnouncementView(generics.CreateAPIView):
    permission_classes = (IsAdmin, )
    serializer_class = AnnouncementSerializer
    queryset = AnnouncementModel.objects.all()


class ListAnnouncementView(generics.ListAPIView):
    permission_classes = (IsAdmin, )
    serializer_class = AnnouncementSerializer
    queryset = AnnouncementModel.objects.all()


class AnnouncementDetailView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (IsAdmin, )
    serializer_class = AnnouncementSerializer
    queryset = AnnouncementModel.objects.all()

class AnnouncementDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    permission_classes = (IsAdmin, )
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


class ParentRegistrationView(RegisterView):
    serializer_class = ParentRegisterationSerializer
    permission_classes = (IsAdmin,)


class Enroll_Parent(APIView):
    '''Only admin can enroll students'''
    permission_classes = (IsAdmin, )

    def post(self, request, format=None):
        serializer = EnrollParentSerializer(data=request.data)
        if serializer.is_valid():
            parent = serializer.validated_data.get('parent', '')
            student = serializer.validated_data.get('student', '')
            Class = serializer.validated_data.get('classes', '')
            course = serializer.validated_data.get('course', '')
            
            if student.school.admin != self.request.user:
                return Response(
                    {'message':'This student is not enrolled in your school'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
            if parent.school.admin != self.request.user:
                return Response(
                    {'message':'This parent is not enrolled in your school'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
            elif Class.school.admin != self.request.user:
                return Response(
                    {'message':'This class is not part of your school'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
            elif course.classes.school.admin != self.request.user:
                return Response(
                    {'message':'This course is not part of your school'}, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

