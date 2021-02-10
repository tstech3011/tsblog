from django.urls import path
from . import views
from .views import (
                    PostListView, 
                    PostDetailView,
                    PostCreateView
                    )

urlpatterns = [
    # path('', views.index, name='index'),
    path('', PostListView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
