from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r"^image/(?P<height>\d+)x(?P<width>\d+)/(?P<url>\S+)$", "utils.views.image", name="utils_image"),
)