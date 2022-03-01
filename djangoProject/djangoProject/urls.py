from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from app01 import views
from rest_framework_jwt.views import obtain_jwt_token
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_jwt_token),  # 登录url，用于获取token
    path('register/', views.RegisterView.as_view()),  # 注册视图,  /user/register/
    path('adduser/',views.adduserList.as_view()),
    path('getuserlist/', views.getuserlist.as_view()),
    path('deluser/', views.deluser.as_view()),
    path('userstate/', views.userstate.as_view()),
    path('updateuser/', views.updateuser.as_view()),

]
