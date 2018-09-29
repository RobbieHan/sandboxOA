from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


from .forms import LoginForm
from .mixin import LoginRequiredMixin

User = get_user_model()

class UserBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class IndexView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'index.html')


class LoginView(View):

    def get(self, request):
        if not request.user.is_authenticated():
            return render(request, 'system/users/login.html')
        else:
            return HttpResponseRedirect('/')

    def post(self, request):
        redirect_to = request.GET.get('next', '/')
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(redirect_to)
                else:
                    msg = "用户未激活！"
                    ret = {"msg": msg, "login_form": login_form}
                    return render(request, 'system/users/login.html', ret)
            else:
                msg = "用户名或密码错误！"
                ret = {"msg": msg, "login_form": login_form}
                return render(request, 'system/users/login.html', ret)
        else:
            msg = "用户名和密码不能为空！"
            ret = {"msg": msg, "login_form": login_form}
            return render(request, "system/users/login.html", ret)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("login"))


