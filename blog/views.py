# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Post
from django.contrib import messages



# Create your views here.
def index(request):
    post_list = Post.objects.order_by('created_date')[:10]
    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context)


def blog(request):
    return render(request, 'blog/blog.html')

def post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'blog/post.html', {'post': post})

def about(request):
    return render(request, 'blog/about.html')
