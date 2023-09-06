from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    # path('<int:post_id>', views.post_details, name='post-details'),
]
