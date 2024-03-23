from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("shop/<int:pk>/", views.shop, name="shop"),
    path("product/<int:pk>/", views.product, name="product"),
]
