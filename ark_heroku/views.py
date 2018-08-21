from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
import firebase_admin
from firebase_admin import credentials, auth, db, firestore, storage
import os
import json
firebase_key = os.environ["FIREBASE"]
cred = credentials.Certificate(json.loads(firebase_key))
firebase_admin.initialize_app(cred)
# For Firebase Functions
# https://console.firebase.google.com/u/2/project/ark-cg/overview?hl=ja


def image_url():


def get_works():
    db = firestore.client()
    data = db.collection(u'works').get()
    return [i.to_dict() for i in data]


def get_news():
    db = firestore.client()
    data = db.collection(u'news').get()
    return [i.to_dict() for i in data]
# Create your views here.


def index(request):
    # トップページ(galary,news,member)
    content = {
        'works': get_works(),
        'news': get_news()
    }
    return render(request, 'index.html', content)


def gallery(request):
    content = {'works': get_works(), }
    return render(request, 'gallery.html', content)


def about(request):
    content = {}
    return render(request, 'about.html', content)


def news(request):
    content = {
        'news': get_news()
    }
    return render(request, 'news.html', content)


def idea(request):
    content = {}
    return render(request, 'idea.html', content)


def progress(request):
    content = {}
    return render(request, 'progress.html', content)


def create(request):
    if request.method == 'POST':
        if 'create_work' in request.POST:
        if 'create_news' in request.POST:
        if 'create_idea' in request.POST:
    context = {
        'cards': new_cards,
        'requests': new_requests,
    }
    return render(request, 'iniita/index.html', context)
