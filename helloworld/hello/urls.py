from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:name_id>/', views.person, name='person'),
]
