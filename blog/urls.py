from . import views
from django.urls import path

"""
Remember the "edit_comment" and "delete _comment" in the urlpattern are not found in our
template neither in our model or our workspace, this are dynamically updated to the URL for
the comment_edit view function and comment_delete view function
"""

urlpatterns = [
    path('', views.PostList.as_view(), name='home'), # as.view() for class-based view
    path('<slug:slug>/', views.post_detail, name='post_detail'), 
    path('<slug:slug>/edit_comment/<int:comment_id>', # The comment form's action attribute points to the URL for the comment_edit view, with the ID of the selected comment
         views.comment_edit, name='comment_edit'), # urls for editing comment
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),# urls for deleting comment
]