from django.urls import path

from . import views

urlpatterns = [
    path('tg_bot/', views.webhook, name='webhook')
]
