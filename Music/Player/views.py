from django.shortcuts import render
from django.views import View
from .models import MusicInfo
from .forms import MusicForm,CustomAuthenticationForm,CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

class CustomLogin(LoginView):
    template_name = "Login.html"
    authentication_form = CustomAuthenticationForm
    form_class = CustomAuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('Player')

class registerPage(FormView):
    template_name = 'register.html'
    authentication_form = CustomUserCreationForm
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('Login')

    def form_valid(self,form):
        user = form.save()
        return super(registerPage,self).form_valid(form)

class Player(View):
    def get(self,request,id):
        Mus = MusicInfo.objects.get(id=id)
        return render(request,'SongPlayer.html',{'song':Mus})

class SongCreate(LoginRequiredMixin,View):
    def get(self,request):
        form=MusicForm()
        return render(request,'Upload.html',{'formupload':form})

    def post(self,request):
        formdata=MusicForm(request.POST,request.FILES)
        formdata.save()
        return HttpResponseRedirect('/')

class GetMusic(View):
    def get(self,request):
        Mu=MusicInfo.objects.all()
        return render(request,'Player.html',{'song':Mu})


class Logout(LogoutView):
    def get(self, request):
        return render(request, 'Login.html', {})
