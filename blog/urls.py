from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'), # as.view() for class-based view
    path('<slug:slug>/', views.post_detail, name='post_detail'), # as for normal function no as.view() is required
]