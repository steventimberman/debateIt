from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login, logout

app_name = 'debate'

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'debate/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'debate/logout.html'}, name='logout'),
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^register/user_profile/$', views.RegisterUserProfile.as_view(), name='register_user_profile'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.ProfileView.as_view(), name='profile_with_pk'),
    url(r'^profile/edit/$', views.profile_edit, name='profile_edit'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'),
    url(r'^find_friends/$', views.FindFriends.as_view(), name='find_friends'),

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'^debate-topic/add/$', views.DebateTopicCreate.as_view(),name='debate-topic-add'),
    url(r'^debate-topic/(?P<pk>[0-9]+)/$', views.DebateTopicCreate.as_view(),name='debate-topic-update'),
    url(r'^debate-topic/(?P<pk>[0-9]+)/delete/$', views.DebateTopicCreate.as_view(),name='debate-topic-delete'),

    url(r'^(?P<pk>[0-9]+)/comment-add/$', views.add_comment_to_post, name='comment-add'),

    url(r'^search/', views.search_titles),

    url(r'^api/', include('debate.api.urls', namespace='debate-api')),
    url(r'^friendship/', include('friendship.urls')),
]