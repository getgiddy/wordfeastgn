from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('posts/<str:slug>/', views.PostDetailView.as_view(),
         name='blog-post-detail'),
    path('create-post/', views.CreatePostView.as_view(), name='create-post'),
    path('delete-post/<str:slug>',
         views.DeletePostView.as_view(), name='delete-post'),
    path('update-post/<str:slug>',
         views.PostUpdateView.as_view(), name='update-post'),
    path('<str:username>/posts/',
         views.AuthorPostListView.as_view(), name='author-posts'),
    path('<str:username>/', views.author_profile, name='author-profile'),
]
