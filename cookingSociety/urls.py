from django.urls import path

from . import views

urlpatterns = [
    # ex: /cookingSociety/
    path('', views.index, name='index'),
    # ex: /cookingSociety/5/
    path('<int:question_id>/', views.detail, name='detail'),

]
