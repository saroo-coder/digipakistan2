from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh-token', TokenRefreshView.as_view(), name='refreshtoken'),
    path('email-submit', emailsubmit.as_view(), name='email-submit'),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),

    path('logout/', LogoutAPIView.as_view(), name='auth_logout'),
#    path('user', UserListView.as_view(), name='userlist'),
#    path('user/<int:pk>/', UserDetalView.as_view() , name = "userdetail"),
    # path('profile', ProfileView.as_view(), name='profile'),
    # path('profile/<int:pk>/', DetailProfileView.as_view() , name = "profile_detail"),
    path('article', ArticleView.as_view(), name='article'),
    path('article/<int:pk>/', DetailArticleView.as_view() , name = "article"),
    path('onlinetest', OnlineTestView.as_view(), name='onlinetest'),
    path('onlinetest/<int:pk>/', DetailRoleView.as_view() , name = "onlinetest"),
    path('announcement', AnnouncementView.as_view(), name='announcement'),
    path('announcement/<int:pk>/', DetailAnnouncementView.as_view() , name = "announcement"),

]
