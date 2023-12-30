from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('<slug:slug>/', views.PostPage.as_view(), name='post_page'),
]