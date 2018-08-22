from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
import firebase_admin
import datetime
from firebase_admin import credentials, auth, db, firestore, storage
import os
import json
firebase_key = os.environ["FIREBASE"]
cred = credentials.Certificate(json.loads(firebase_key))
firebase_admin.initialize_app(cred)
db = firestore.client()

# For Firebase Functions
# https://console.firebase.google.com/u/2/project/ark-cg/overview?hl=ja


def image_url(locate_url):
    return 0


def get_works():
    data = db.collection(u'works').get()
    return [i for i in data]


def get_news():
    data = db.collection(u'news').get()
    return [i for i in data]


# Create your views here.


def index(request):
    # トップページ(galary,news,member)
    content = {'works': get_works(), 'news': get_news()}
    return render(request, 'index.html', content)


def gallery(request):
    content = {
        'works': get_works(),
    }
    return render(request, 'gallery.html', content)


def about(request):
    content = {}
    return render(request, 'about.html', content)


def news(request):
    content = {'news': get_news()}
    return render(request, 'news.html', content)


def idea(request):
    content = {}
    return render(request, 'idea.html', content)


def progress(request):
    content = {}
    return render(request, 'progress.html', content)


def create(request):
    if request.method == 'POST':
        data = {
            'title': request.Form('title'),
            'context': request.Form('context'),
            'image': image_url(request.FILES['file']),
            'date': datetime.datetime.now(),
            'timestamp': datetime.datetime.now(),
        }
        if request.Form('radio-grp') == 'gallery':
            db.collection(u'works').add(data)
        elif request.Form('radio-grp') == 'news':
            db.collection(u'news').add(data)
        elif request.Form('radio-grp') == 'idea':
            db.collection(u'ideas').add(data)
    content = {}
    return render(request, 'create.html', content)


def detail(request, id):
    data = db.collection(u'works').documents(id).get()
    data = data.to_dict()
    content = {
        'work': data,
    }
    return render(request, 'detail.html', content)
