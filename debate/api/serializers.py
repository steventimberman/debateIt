from rest_framework.serializers import ModelSerializer

from debate.models import DebateTopic

class DebateTopicSerializer(ModelSerializer):
    class Meta:
        model = DebateTopic
        fields = [
            'topic',
            'description',
            'timestamp',
            'photo',
            'article_URL',
            'user'
        ]