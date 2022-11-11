from django.urls import path
from .views import BlogHomeView, PostDetailView


urlpatterns = [
    path('blog/',BlogHomeView.as_view(),name="blog-home"),
    path('blog/post/<int:pk>/',PostDetailView.as_view(),name="post-detail")
]