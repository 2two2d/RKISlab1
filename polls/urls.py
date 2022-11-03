from django.urls import re_path as path

from . import views



urlpatterns = [
    path(r'^$', views.all_q, name='index'),
    path(r'^register/$', views.register, name='register'),
    path(r'^myQuestions/$', views.my_q, name='my_q'),
    path(r'^addQuestion/$', views.add_q, name='add_q'),
    path(r'^<int:pk>/addOptions/$', views.add_options, name='add_options'),
    path(r'^myProfile/$', views.my_profile, name='my_profile'),
    path(r'^<int:pk>/$', views.DetailView.as_view(), name='detail'),
    path(r'^<int:pk>/results/$', views.ResultsView.as_view(), name='results'),
    path(r'^<int:question_id>/vote/$', views.vote, name='vote'),
    path(r'^user_delete/$', views.UserDelete, name='user_delete'),
    path(r'^user_edit/$', views.update_user, name='user_update')
]