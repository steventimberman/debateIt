import datetime
from haystack import indexes
from debate.models import DebateTopic

class DebateTopicIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    pub_date = indexes.DateTimeField(model_attr='timestamp')

    content_auto = indexes.EdgeNgramField(model_attr='topic')

    def get_model(self):
        return DebateTopic

    def index_queryset(self, using=None):
        return self.get_model().objects.all()