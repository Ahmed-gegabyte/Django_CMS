from django.contrib import admin
from django.urls import path ,include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article_list/', views.article_list, name='article_list'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),  # URL for article details
    path('add-article/', views.add_article, name='add_article'),
    path('article/<int:article_id>/edit/', views.article_update, name='article_update'),  # Update path
    path('article/<int:article_id>/delete/', views.article_delete, name='article_delete'),  # Delete path
    
]