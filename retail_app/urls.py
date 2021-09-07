from . import views
from django.urls import path

urlpatterns = [
    path('stores', views.StoreList.as_view()),
    path('stores/<int:pk>', views.StoreDetail.as_view()),
]