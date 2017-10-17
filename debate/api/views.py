from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView
    )
from debate.models import DebateTopic
from debate.api.serializers import DebateTopicSerializer

class DebateTopicListAPIView(ListAPIView):
    queryset = DebateTopic.objects.all()
    serializer_class = DebateTopicSerializer

class DebateTopicDetailAPIView(RetrieveAPIView):
    queryset = DebateTopic.objects.all()
    serializer_class = DebateTopicSerializer

class DebateTopicEditAPIView(UpdateAPIView):
    queryset = DebateTopic.objects.all()
    serializer_class = DebateTopicSerializer

class DebateTopicDeleteAPIView(DestroyAPIView):
    queryset = DebateTopic.objects.all()
    serializer_class = DebateTopicSerializer

