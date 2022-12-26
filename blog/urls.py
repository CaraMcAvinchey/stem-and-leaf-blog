from . import views
from django.urls import path


urlpatterns = [
    path('', views.PlantList.as_view(), name='home'),
    path('<slug:slug>/', views.PlantDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/<int:pk>/delete_comment/',
         views.CommentDelete.as_view(), name="delete_comment"),
    path('<slug:slug>/<int:pk>/edit_comment/',
         views.CommentEdit.as_view(), name="edit_comment"),
    path('404', views.Page403.as_view(), name='403'),
    path('404', views.Page404.as_view(), name='404'),
    path('500', views.Page500.as_view(), name='500'),
]
