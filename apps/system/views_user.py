from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic.base import View
from django.http import HttpResponseRedirect



class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')


class LoginView(View):

    def get(self, request):
        if not request.user.is_authenticated():
            return render(request, 'system/users/login.html')
        else:
            return HttpResponseRedirect('/')