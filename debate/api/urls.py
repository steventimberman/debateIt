from django.conf.urls import url
from django.contrib import admin
from debate.api.views import (
    DebateTopicListAPIView,
    DebateTopicDetailAPIView,
    DebateTopicEditAPIView,
    DebateTopicDeleteAPIView
)

urlpatterns = [
    url(r'^$', DebateTopicListAPIView.as_view(), name='debate-list'),
    url(r'^(?P<pk>\d+)/$', DebateTopicDetailAPIView.as_view(), name='debate-list'),
    url(r'^(?P<pk>\d+)/edit/$', DebateTopicEditAPIView.as_view(), name='debate-update'),
    url(r'^(?P<pk>\d+)/delete/$', DebateTopicDeleteAPIView.as_view(), name='debate-delete')

]