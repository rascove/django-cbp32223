from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Issue(models.Model):
    type = models.CharField(max_length = 100, choices = [('Hardware', 'Hardware'), ('Software', 'Software')])
    room = models.CharField(max_length = 100)
    urgent = models.BooleanField(default = False)
    details = models.TextField()
    date_submitted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('itreporting:issue-detail', kwargs = {'pk': self.pk})