from django.urls import path
from .import views


urlpatterns = [
    path("", views.index, name="SHOPHOME"),
    path("about/", views.about, name="About Us"),
    path("contact/", views.contact, name="contact Us"),
    path("tracker/", views.tracker, name="track Us"),
    path("Products/<int:myid>", views.productview, name="ProductView"),
    path("feedback/", views.feedback, name="Thank you Us"),
    path("instagram", views.instagram, name="Instagram"),
    path("phone", views.phone, name="Phone"),
    path("email", views.email, name="Email"),
]
