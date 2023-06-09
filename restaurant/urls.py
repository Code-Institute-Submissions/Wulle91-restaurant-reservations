"""restaurant URL Configuration

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
from django.urls import path, include
from reservations.views import sho_dates, comments, delete_comment, edit_reservation, delete_reservation

urlpatterns = [
    path('edit/<date_id>', edit_reservation, name='edit'),
    path('delete_comment/<comment_id>', delete_comment, name='delete_comment'),
    path('delete/<date_id>', delete_reservation, name='delete'),
    path('admin/', admin.site.urls),
    path('', comments, name='home'),
    path('accounts/', include('allauth.urls')),
    path('reservations', sho_dates, name='dates'),
]
