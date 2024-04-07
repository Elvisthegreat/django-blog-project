from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'), # as.view() for class-based view
    path('<slug:slug>/', views.post_detail, name='post_detail'), 
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'), # urls for editing comment
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),# urls for deleting comment
]