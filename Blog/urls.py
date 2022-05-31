from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('bonjour', views.bonjour, name='bonjour'),
	path('post/<int:pk>/', views.post_detail, name='post_detail')
]