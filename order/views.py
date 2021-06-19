from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse

class Pay(View):
    def get(self, *args, **kargs):
        return HttpResponse('pague o aluguel')


class Close(View):
    def get(self, *args, **kargs):
        return HttpResponse('fecha')


class Detail(View):
    def get(self, *args, **kargs):
        return HttpResponse('detalhe')
