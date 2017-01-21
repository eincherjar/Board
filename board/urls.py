from django.conf.urls import url
from . import views

app_name = 'board'

urlpatterns = [
    url(r'^$', views.BoardIndexView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^(?P<pk>[0-9]+)/$', views.BoardDetailView.as_view(), name='detail'),
]