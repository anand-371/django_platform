from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from django.conf import	settings
from django.conf.urls.static import static	
urlpatterns=[
		path('',PostListView.as_view(),name='blog-home'),
		path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
		path('post/new',PostCreateView.as_view(),name='post-create'),
		path('post/<int:pk>/update',PostUpdateView.as_view(),name='post-update'),
		path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post-delete'),
		path('about/',views.about,name='blog-about'),
		path('like/',views.like_post,name='like_post'),
]

