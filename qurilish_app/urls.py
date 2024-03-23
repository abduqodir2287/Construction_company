from django.urls import path
from .views import *

urlpatterns = [
    path("hello/", hello, name="hello"),
    path("", home, name="home"),
    path("about_us/", about_us, name="about_us"),
    path("services/", services, name="services"),
    path("our_works/", our_works, name="our_works"),
    path("contacts/", contacts, name="contacts"),
]

