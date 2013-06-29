from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponse, HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse
from django.utils import simplejson as json
from django.contrib.flatpages.views import render_flatpage
from django.utils.translation import ugettext_lazy as _
from django.db import IntegrityError
from orzubalsky.utils import unique_slugify
from orzubalsky.models import *
from orzubalsky.forms import *


def home(request):
    """
    """
    return render_to_response('home.html',{ }, context_instance=RequestContext(request))