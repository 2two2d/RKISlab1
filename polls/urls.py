from django.urls import re_path as path

from . import views



urlpatterns = [
    path(r'^$', views.IndexView.as_view(), name='index'),
    path(r'^register/$', views.register, name='register'),
    path(r'^my_profile/$', views.my_profile, name='my_profile'),
    path(r'^<int:pk>/$', views.DetailView.as_view(), name='detail'),
    path(r'^<int:pk>/results/$', views.ResultsView.as_view(), name='results'),
    path(r'^<int:question_id>/vote/$', views.vote, name='vote'),
    path(r'^user_delete$', views.UserDelete, name='user_delete')
]