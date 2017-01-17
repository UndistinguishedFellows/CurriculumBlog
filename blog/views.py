# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Post



# Create your views here.
def index(request):
    post_list = Post.objects.order_by('created_date')[:5]
    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context)


def post_page(request):
    return render(request, 'blog/blog.html')

def author(request):
    return render(request, 'blog/about.html')
