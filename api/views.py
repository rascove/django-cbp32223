from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from itreporting.models import Issue
from .serializers import IssueSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class IssueViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Issue.objects.all().order_by('date_submitted')
    serializer_class = IssueSerializer

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)