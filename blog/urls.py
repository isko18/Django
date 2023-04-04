from django.urls import path
from blog import views
urlpatterns = [
    path("hello/", views.get_hello, name="Hello-view"),
    path("contacts/", views.get_contacts, name="Contacts-view"),
    path("about/", views.get_about, name="About-view"),
]