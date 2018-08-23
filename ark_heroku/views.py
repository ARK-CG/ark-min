from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
import firebase_admin
import time, datetime
from firebase_admin import credentials, auth, firestore, storage
import os
import json
firebase_key = os.environ["FIREBASE"]
cred = credentials.Certificate(json.loads(firebase_key))
firebase_admin.initialize_app(cred, {'storageBucket': 'ark-cg.appspot.com'})
db = firestore.client()

# For Firebase Functions
# https://console.firebase.google.com/u/2/project/ark-cg/overview?hl=ja


def image_url(types, locate_url):
    filename = str(time.time())
    blob = storage.bucket().blob(types + filename + locate_url[-4:])
    blob.upload_from_filename(locate_url)
    blob.make_public()
    return blob.public_url


def get_data(data_type):
    data = list(db.collection(data_type).get())
    datas = [i.to_dict() for i in data]
    ids = [k.id for k in data]
    [datas[i].update(id=ids[i]) for i in range(len(ids))]
    return datas


# Create your views here.


def index(request):
    # トップページ(galary,news,member)
    content = {'works': get_data('works'), 'news': get_data('news')}
    return render(request, 'index.html', content)


def gallery(request):
    content = {
        'works': get_data('works'),
    }
    return render(request, 'gallery.html', content)


def about(request):
    content = {}
    return render(request, 'about.html', content)


def news(request):
    content = {'news': get_data('news')}
    return render(request, 'news.html', content)


def idea(request):
    content = {}
    return render(request, 'idea.html', content)


def progress(request):
    content = {}
    return render(request, 'progress.html', content)


def create(request):
    if request.method == 'POST':
        types = request.POST['radio-grp']
        data = {
            'title': request.POST['title'],
            'context': request.POST['context'],
            'image': image_url(types, request.FILES['file']),
            'date': datetime.datetime.now(),
            'timestamp': datetime.datetime.now(),
        }
        db.collection(types).set(data)
        return HttpResponseRedirect(reverse(index))
    content = {}
    return render(request, 'create.html', content)


def detail(request, id):
    data = db.collection(u'works').document(id).get()
    content = {
        'work': data.to_dict(),
    }
    return render(request, 'detail.html', content)
