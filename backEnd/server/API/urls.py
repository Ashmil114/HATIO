from django.urls import path,include
from .views import Home

# API Routes

urlpatterns = [
    path('',Home),
    path('api/user/',include('user.urls')),
    path('api/projects/',include('project.urls')),
    path('api/todos/',include('todos.urls')),
    
]