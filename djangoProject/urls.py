from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('execute_script/<int:vm_id>/', views.execute_script, name='execute_script'),
]
