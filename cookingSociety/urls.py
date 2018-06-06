from django.urls import path

from . import views

urlpatterns = [
    # ex: /cookingSociety/
    path('', views.index, name='index'),
    # ex: /cookingSociety/cooker/5/
    path('cooker/<int:cooker_id>/', views.cooker_detail, name='cooker_detail'),
    # ex: /cookingSociety/dish/5/
    # path('dish/<int:dish_id>/', views.dish_detail, name='dish_detail'),
    # ex: /cookingSociety/cooker_create/
    path('cooker_create/', views.cooker_create, name='cooker_create'),
    # ex: /cookingSociety/cooker_new/
    path('cooker_new/', views.cooker_new, name='cooker_new'),

]
