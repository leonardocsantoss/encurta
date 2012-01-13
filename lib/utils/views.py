# -*- coding:utf-8 -*-
from django.http import HttpResponse, Http404
import urllib2
from PIL import Image, ImageFile
from cStringIO import StringIO
from django.conf import settings


def image(request, height, width, url):
    try:
        if 'http://' in url or 'https://' in url:
            inStream = urllib2.urlopen(url)
            response = HttpResponse(mimetype=inStream.info()['Content-Type'])
            response['Last-Modified'] = inStream.info()['Last-Modified']
            p = ImageFile.Parser()
            p.feed(inStream.read())
            im = p.close()
            if im.mode != "RGB":
                im = im.convert("RGB")
        else:
            response = HttpResponse(mimetype='image')
            im = Image.open(u'%s/%s' % (settings.MEDIA_ROOT, url))

        ext = url.split('.')[-1].upper()
        if ext == 'JPG':
            ext = 'JPEG'
        im.thumbnail((int(height),int(width)), Image.ANTIALIAS)
        img_temp = StringIO()
        im.save(img_temp, ext)
        img_temp.seek(0)

        response.write(img_temp.getvalue())
        return response
    except:
        raise Http404()