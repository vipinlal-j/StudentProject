from django.conf.urls import url
from StudApp import views

urlpatterns = [
    url(r'^Student/$', views.StudentAPI),
    url(r'^Student/([0-9]+)/$', views.StudentAPI)

]