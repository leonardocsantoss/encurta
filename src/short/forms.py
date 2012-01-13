# -*- coding:utf-8 -*-
from django import forms
from models import Url


class UrlForm(forms.ModelForm):

    class Meta:
        model = Url
        exclude = ('codigo', 'data_de_criacao', 'numero_visitas', )