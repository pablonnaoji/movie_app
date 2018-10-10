#from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^', views.MovieList.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'<int:pk>/', views.MovieDetail.as_view()),
]