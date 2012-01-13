# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.db.models import signals
from django.conf import settings
from django.utils.translation import ugettext as _
import random
from django.core.urlresolvers import reverse


def gera_codigo():
    codigo = ""
    for x in range(settings.NUMBER_SHORT):
        codigo += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
    return codigo


class Url(models.Model):

    url = models.URLField(max_length=255, unique=True, verbose_name=_(u"Url"))
    codigo = models.CharField(blank=True, unique=True, max_length=20, verbose_name=_(u"Código"))
    data_de_criacao = models.DateTimeField(default=datetime.now, verbose_name=_(u"Data de cricação"))
    numero_visitas = models.PositiveIntegerField(default=0, verbose_name=_(u"Número de visitas"))
    
    class Meta:
        ordering = ('-numero_visitas',)

    def get_absolute_url(self):
        return reverse('short.views.view',kwargs={'codigo': self.codigo})

    def acoes(self):
        a1 = u"<a href=\"%s\" style=\"padding-left: 7px;\" >Editar</a>" % (self.pk, )
        a2 = u"<a style=\"padding-left: 7px;\" href=\"javascript://\" onClick=\"(function($) { $('input:checkbox[name=_selected_action]').attr('checked', ''); $('input:checkbox[name=_selected_action][value=%s]').attr('checked', 'checked'); $('select[name=action]').attr('value', 'delete_selected'); $('#changelist-form').submit(); })(jQuery);\" >Remover</a>" % (self.pk, )
        return a1+a2
    acoes.allow_tags = True
    acoes.short_description = u"Ações"

    def __unicode__(self):
        return u"%s" % (self.url)

def cria_codigo(sender, instance=None, **kwargs):
    if instance is None:
        return
    if not instance.codigo:
        codigo = gera_codigo()
        while(len(Url.objects.filter(codigo=codigo))):
            codigo = gera_codigo()
        instance.codigo = codigo
signals.pre_save.connect(cria_codigo, sender=Url)