from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    # トップページ(galary,news,member)
    content = {
    }
    return render(request, 'index.html', content)


def gallery(request):
    content = {}
    return render(request, 'gallery.html', content)


def about(request, id):
    content = {

    }
    return render(request, 'about.html', content)


def news(request):
    content = {}
    return render(request, 'news.html', content)


def idea(request):
    content = {}
    return render(request, 'idea.html', content)


def progress(request):
    content = {}
    return render(request, 'progress.html', content)
