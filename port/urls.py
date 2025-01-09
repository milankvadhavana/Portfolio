from django.urls import path
from port.views import index,project_details

urlpatterns = [
    path('', index, name='index'),
    path('details/<int:pk>/',project_details, name='project_details'),    
]
