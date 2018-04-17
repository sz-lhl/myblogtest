#coding:utf8
import markdown
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    #return HttpResponse('welecom')
    """
我们首先把 HTTP 请求传了进去，然后 render 根据第二个参数的值 blog/index.html
找到这个模板文件并读取模板中的内容。 render 传入的 context 参数值把模板变量，
{{ title }} 被替换成了 context 字典中 title 对应的值，
同理 {{ welcome }} 也被替换成相应的值。
最终，我们的 HTML 模板中的内容字符串
被传递给 HttpResponse 对象并返回给浏览器（Django 在 render 函数里
隐式地帮我们完成了这个过程），这样用户的浏览器上便显示出了
我们写的 HTML 模板的内容。
    """
    """
    return render(request,'blog/index.html',context={
                    'title':'我的博客首页',
                    'welcome':'欢迎访问',
                    })
    """
    post_list = Post.objects.all().order_by('-create_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                      ])
    return render(request,'blog/detail.html',context={'post':post})
