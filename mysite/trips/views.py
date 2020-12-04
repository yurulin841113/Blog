from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from .models import Post


# Create your views here.
def hello(request):
    return render(request, 'hello.html', {
        'current_time': str(datetime.now()),
    })


def home(request):
    post = Post.objects.all()
    return render(request, 'home.html', {
        'post_list': post,
    })


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {
        'post_detail': post,
    })
