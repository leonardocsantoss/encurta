# -*- coding:utf-8 -*-
from django.test import TestCase
from django.test.client import Client
from django.conf import settings
from django.core.urlresolvers import reverse

from short.models import Url




class TesteShort(TestCase):
    def setUp(self):
        self.url, created = Url.objects.get_or_create(url='http://google.com.br')
        self.url1, created = Url.objects.get_or_create(url='http://iellos.com')
        self.url2, created = Url.objects.get_or_create(url='http://sodavirtual.com.br')
        self.client = Client(enforce_csrf_checks=True)


    def testCreateObjects(self):
        self.assertEquals(Url.objects.count(), 3)
        
        self.assertTrue(self.url.codigo)
        self.assertEquals(len(self.url.codigo), settings.NUMBER_SHORT)
        self.assertEquals(self.url.numero_visitas, 0)

        self.assertTrue(self.url1.codigo)
        self.assertEquals(len(self.url1.codigo), settings.NUMBER_SHORT)
        self.assertEquals(self.url1.numero_visitas, 0)

        self.assertTrue(self.url2.codigo)
        self.assertEquals(len(self.url2.codigo), settings.NUMBER_SHORT)
        self.assertEquals(self.url2.numero_visitas, 0)


    def testIndexViews(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)


    def testShortViews(self):
        #Url normal
        response = self.client.post(reverse('short'), {'url': 'g1.com.br'})
        self.assertEquals(response.status_code, 200)

        self.assertEquals(Url.objects.count(), 4)

        #Mesma url
        response2 = self.client.post(reverse('short'), {'url': 'g1.com.br'})
        self.assertEquals(response2.status_code, 200)
        self.assertEquals(response.content, response2.content)

        #Url errada
        response3 = self.client.post(reverse('short'), {'url': 'dasdasdasd'})
        self.assertEquals(response3.status_code, 404)

        #Por get
        response4 = self.client.get(reverse('short'), {'url': 'g1.com.br'})
        self.assertEquals(response4.status_code, 404)


    def testViewViews(self):
        #Visitar cada link, e ver se ele redirecionou para o local certo
        response = self.client.get(reverse('view', args=[self.url.codigo]), follow=True)
        self.assertEquals(response.redirect_chain[0][0], self.url.url)

        response1 = self.client.get(reverse('view', args=[self.url1.codigo]), follow=True)
        self.assertEquals(response1.redirect_chain[0][0], self.url1.url)

        response2 = self.client.get(reverse('view', args=[self.url2.codigo]), follow=True)
        self.assertEquals(response2.redirect_chain[0][0], self.url2.url)

        self.setUp()

        #Numero de visitas
        self.assertEquals(self.url.numero_visitas, 1)
        self.assertEquals(self.url1.numero_visitas, 1)
        self.assertEquals(self.url2.numero_visitas, 1)