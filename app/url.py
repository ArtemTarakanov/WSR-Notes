from django.contrib import admin

from . import views
from django.urls import path

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("articles/", views.ArticleList.as_view(), name="article"),
    path("articles/<int:pk>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("articles/create/", views.ArticleCreate.as_view(), name="article-create"),
    path("articles/<int:pk>/update/", views.ArticleUpdate.as_view(), name="article-update"),
    path("articles/<int:pk>/delete/", views.ArticleDelete.as_view(), name="article-delete"),
    path('register/', views.Registration.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name="profile"),
    path('profile/edit', views.ProfileUpdateView.as_view(), name="profile-edit"),
    path('profile/delete', views.UserDelete.as_view(), name="user-delete")

]