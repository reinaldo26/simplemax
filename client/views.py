from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View

class Create(View):
    def get(self, *args, **kargs):
        return HttpResponse('criar')


class Update(View):
    def get(self, *args, **kargs):
        return HttpResponse('atualizar')


class Login(View):
    def get(self, *args, **kargs):
        return HttpResponse('login')


class Logout(View):
    def get(self, *args, **kargs):
        return HttpResponse('logout')
