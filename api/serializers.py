from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer, SlugRelatedField
from itreporting.models import Issue

class IssueSerializer(HyperlinkedModelSerializer):
    author = SlugRelatedField(slug_field = 'username', queryset = User.objects.all())

    class Meta:
        model = Issue
        fields = ['type', 'room', 'urgent', 'details', 'date_submitted', 'author']