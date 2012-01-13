# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Url


class AdminUrl(admin.ModelAdmin):

    list_display = ('url', 'codigo', 'data_de_criacao', 'numero_visitas', 'acoes' )
    list_filter = ('data_de_criacao', 'numero_visitas' )
    search_fields = ('url', )
    date_hierarchy = 'data_de_criacao'

    list_report = ('url', 'codigo', 'data_de_criacao', 'numero_visitas' )

    fieldsets = (
        (u"Url",             {"fields" : ('url', 'codigo', 'data_de_criacao', 'numero_visitas' ), }, ),
    )

admin.site.register(Url, AdminUrl)
