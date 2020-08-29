from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod, ReadDetail


# 博客类别
class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):  # 主要是添加这个魔法函数，使得博客类型可视，不然选择时下拉都是什么object1之类的
        return self.type_name


# 博文
class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=50)  # 标题
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE)  # 博客类别，接入外键
    content = RichTextUploadingField()  # 博客内容
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 博客作者，接入django自带的外键
    read_details = GenericRelation(ReadDetail)
    created_time = models.DateTimeField(auto_now_add=True)  # 博客创建时间
    last_updated_time = models.DateTimeField(auto_now=True)  # 博客最新更新时间

    """
        def get_read_num(self):
        try:
            return self.readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0
    """
    def get_url(self):
        return reverse('blog_detail', kwargs={'blog_pk': self.pk})

    def get_email(self):
        return self.author.email

    def __str__(self):  # 这个也添加上
        return "<Blog: %s>" % self.title

    class Meta:
        ordering = ['-created_time']

"""
class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
"""
