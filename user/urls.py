from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login_user'),  # 别名最好不要和url字段重复，，不然href写法不使用别名的写法会报错
    path('login_for_medal/', views.login_for_medal),
    path('register/', views.register),
    path('logout/', views.logout),
    path('user_info/', views.user_info),
    path('change_nickname/', views.change_nickname),
    path('bind_email/', views.bind_email),
    path('send_verification_code/', views.send_verification_code),
    path('change_password/', views.change_password),
    path('forgot_password/', views.forgot_password),
]