from django.urls import path
from .views import home, about, ContactFormView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

app_name = 'itreporting'
urlpatterns = [
    path('', home, name = 'home'),
    path('about', about, name = 'about'),
    path('report', PostListView.as_view(), name = 'report'),
    path('contact', ContactFormView.as_view(), name = 'contact'),
    path('issue/<int:pk>', PostDetailView.as_view(), name = 'issue-detail'),
    path('issue/new', PostCreateView.as_view(), name = 'issue-create'),
    path('issue/<int:pk>/update', PostUpdateView.as_view(), name = 'issue-update'),
    path('issue/<int:pk>/delete', PostDeleteView.as_view(), name = 'issue-delete'),
    path('issue/<str:username>', UserPostListView.as_view(), name = 'user-issues'),
]