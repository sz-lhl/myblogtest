#coding:utf8
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

# Create your models here.
# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    """
    Django 要求模型必须继承 models.Model 类。
    Category 只需要一个简单的分类名 name 就可以了。
    CharField 指定了分类名 name 的数据类型，CharField 是字符型，
    CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
    当然 Django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
    Django 内置的全部类型可查看文档：
    https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
    """
   
# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class Tag(models.Model):
    """
    标签 Tag 也比较简单，和 Category 一样。
    再次强调一定要继承 models.Model 类！
    """
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class Post(models.Model):
    
    title = models.CharField(max_length=70)
    body = models.TextField()

    create_time=models.DateTimeField()
    modified_time = models.DateTimeField()
#允许空值
    excerpt = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Category)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})
    # reverse 函数，
    #它的第一个参数的值是 'blog:detail'，意思是 blog 应用下的 name=detail 的函数
    #多对多关系
    """

文章 ID	标签 ID
1	1
1	2
2	1
3	2
多对多的关系无法再像一对多的关系中的例子一样在文章数据库表加一列 分类 ID 来关联了，
因此需要额外建一张表来记录文章和标签之间的关联。
例如文章 ID 为 1 的文章，
既对应着 标签 ID 为 1 的标签，也对应着 标签 ID 为 2 的标签，
即文章 1 既属于标签 1：Django 学习，也属于标签 2：Python 学习。
    """
    tags = models.ManyToManyField(Tag,blank=True)
    #这里规定一个文章只有一个作者，而作者可以写多个文章，
    #user从django.contrib.auth.models导入
    author = models.ForeignKey(User)
    
    
