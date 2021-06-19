from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View

class ProdutcList(View):
    def get(self, *args, **kargs):
        return HttpResponse('lista')


class ProdutcDetail(View):
    def get(self, *args, **kargs):
        return HttpResponse('detalhe prod')


class AddToCart(View):
    def get(self, *args, **kargs):
        return HttpResponse('add to carrinho')


class RemoveFromCart(View):
    def get(self, *args, **kargs):
        return HttpResponse('remove do cart')


class Cart(View):
    def get(self, *args, **kargs):
        return HttpResponse('cart')


class Finish(View):
    def get(self, *args, **kargs):
        return HttpResponse('finalizar')
