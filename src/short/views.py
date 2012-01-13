# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from models import Url
from forms import UrlForm

@csrf_exempt
def short(request, form=UrlForm):
    if request.method == "POST":
        try:
            try:
                url = request.POST['url']
                if not 'http' in url[0:4]: url = 'http://'+url
                if '/' != url[-1]: url = url+'/'
                new_url = Url.objects.get(url=url)
                return HttpResponse(new_url.get_absolute_url())
            except:
                url_form = form(request.POST)
                if url_form.is_valid():
                    new_url = url_form.save()
                return HttpResponse(new_url.get_absolute_url())
        except:
            raise Http404()
    else:
        raise Http404()


def view(request, codigo):
    try:
        url = Url.objects.get(codigo=codigo)
        url.numero_visitas = url.numero_visitas+1
        url.save()
        return HttpResponseRedirect(url.url)
    except:
        raise Http404()
