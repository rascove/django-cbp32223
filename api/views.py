from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from itreporting.models import Issue
from .serializers import IssueSerializer

# Create your views here.
class IssueViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Issue.objects.all().order_by('date_submitted')
    serializer_class = IssueSerializer