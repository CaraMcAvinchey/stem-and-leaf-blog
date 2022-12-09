from . import views
from django.urls import path


urlpatterns = [
    path('', views.PlantList.as_view(), name='home'),
    path('<slug:slug>/', views.PlantDetail.as_view(), name='post_detail'),
]
