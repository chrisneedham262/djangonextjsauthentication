from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.customerRegister, name="customer-register"),
    path("me/", views.currentUser, name="current_user"),
    path("me/update/", views.updateUser, name="update_user"),
]
