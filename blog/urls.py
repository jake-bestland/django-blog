from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.detail, name='detail'),
]
