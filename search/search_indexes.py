from django.utils import timezone
from haystack import indexes
from search.models import Show

class ShowIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    time = indexes.DateTimeField(model_attr="time")
    
    def get_model(self):
        return Show

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(time__gte=timezone.now())