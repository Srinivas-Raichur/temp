from django.urls import path
from .views import view_post
urlpatterns = [
    path('upload',view_post.as_view())
]