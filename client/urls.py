from django.urls import path
from .import views

urlpatterns = [
    path('mijoz/',views.MijozListCreateApiView.as_view())
]