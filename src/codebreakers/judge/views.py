# Create your views here.

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponsePermanentRedirect, Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template.loader import get_template
from django.template import RequestContext
from datetime import datetime
from django.contrib import auth
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from django.utils import simplejson

from judge.models import Problem

def code(request):
    t = get_template('arena.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

