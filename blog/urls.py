from django.urls import path
from . import views

# start with blog
urlpatterns = [
    # http://localhost:8000/blog/实际访问地址是这一条加上下面的参数
    path('', views.blog_list, name='blog_list'),
    path('<int:blog_pk>', views.blog_detail, name="blog_detail"),
    path('type/<int:blog_type_pk>', views.blogs_with_type, name="blogs_with_type"),
    path('date/<int:year>/<int:month>', views.blogs_with_date, name='blogs_with_date'),
]