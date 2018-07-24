from django.urls import path
from . import  views

urlpatterns = [
    # ex: /devprofs/
    path('', views.index, name='index'),
    # ex: /devprofs/developer/5/
    path('developer/<int:dev_id>/', views.developer, name='developer'),
    # ex: /devprofs/project/2/
    path('project/<int:proj_id>/', views.project, name='project'),
]