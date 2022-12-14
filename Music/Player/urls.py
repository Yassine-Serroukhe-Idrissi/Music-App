from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('login/',views.CustomLogin.as_view(),name='Login'),
    path('',views.GetMusic.as_view(),name='Player'),
    path('upload/',views.SongCreate.as_view(),name='Upload'),
    path('play/<int:id>',views.Player.as_view(),name='MusicPlayer'),
    path('logout/',views.Logout.as_view(next_page='Login'),name='Logout'),
    path('register/', views.registerPage.as_view(), name='Register'),
]

