from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    # path('', views.index, name='index'),
    path('', PostListView.as_view(), name='posts'),
    path('<int:pk>', PostDetailView.as_view(), name='post'),
]
