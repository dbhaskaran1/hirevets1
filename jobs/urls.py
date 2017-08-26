from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^viewjobs$', views.viewjobs, name='viewjobs'),
    url(r'^addjobs$', views.addjobs, name='addjobs'),
]
