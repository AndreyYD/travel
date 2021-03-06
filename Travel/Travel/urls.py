"""Travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_routes.views import (
    route_view, find_routes, add_route, save_route, RouteListView, RouteDetailView, RouteDeleteView
)
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', route_view, name='home'),
    path('cities/', include('app_cities.urls', namespace='cities')),
    path('trains/', include('app_trains.urls', namespace='trains')),
    path('accounts/', include('app_accounts.urls', namespace='accounts')),
    path('find_routes/', find_routes, name='find_routes'),
    path('add_route/', add_route, name='add_route'),
    path('save_route/', save_route, name='save_route'),
    path('list/', RouteListView.as_view(), name='list'),
    path('routes/<int:pk>/', RouteDetailView.as_view(), name='route'),
    path('routes/delete/<int:pk>/', RouteDeleteView.as_view(), name='delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
