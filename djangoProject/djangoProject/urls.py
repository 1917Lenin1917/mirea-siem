from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import SimpleRouter
from .views import ScriptsView, execute_script, VMView

scripts = SimpleRouter()
scripts.register('scripts', ScriptsView, 'script')


vms = SimpleRouter()
vms.register('vms', VMView, 'vm')


urlpatterns = [
    # path('', views.index, name='index'),
    path('execute_script/<int:vm_id>/', execute_script, name='execute_script'),
    # path('scripts/', ScriptsView.as_view(), name='scripts'),
    path('', include(scripts.urls)),
    path('', include(vms.urls)),
    # path('vms/', VMView.as_view(), name='vms'),
    path('admin/', admin.site.urls)
]
