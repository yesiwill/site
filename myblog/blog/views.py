from django.shortcuts import render
from blog.models import BlogsPost

# Create your views here.

def blog_index(request):
    blog_list = BlogsPost.objects.all()                 #获取所需数据
    return render(request, 'index.html', {'blog_list': blog_list})      #返回渲染后的模板
