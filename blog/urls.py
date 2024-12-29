from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"), #as_view when using class-based views
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]