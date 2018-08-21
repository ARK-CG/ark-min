from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post, News, Idea

# Create your views here.


def index(request):
    # トップページ(galary,news,member)
    posts = Post.objects.order_by('-pub_date')
    news = News.objects.order_by('-pub_date')
    ideas = Idea.objects.order_by('pub_date')
    content = {
        'posts': posts,
        'news': news,
        'ideas': ideas,
    }
    return render(request, 'ark_web/index.html', content)


def gallery(request):
    posts = Post.objects.order_by('-pub_date')
    content = {'posts': posts}
    return render(request, 'ark_web/gallery.html', content)


def about(request, id):
    work = Post.objects.get(id=id)
    content = {
        'title': work.title,
        'context': work.body,
        'date': work.pub_date,
        'user': work.user,
        'image': work.image,
    }
    return render(request, 'ark_web/about.html', content)


def news(request):
    newss = News.objects.order_by('-pub_date')
    content = {'newss': newss}
    return render(request, 'ark_web/news.html', content)


def idea(request):
    ideas = News.objects.order_by('-pub_date')
    content = {'ideas': ideas}
    return render(request, 'ark_web/idea.html', content)


def progress(request):
    idea = Idea.objects.order_by('-pub_date')
    content = {'idea': idea}
    return render(request, 'ark_web/progress.html', content)
