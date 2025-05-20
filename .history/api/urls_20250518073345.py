from rest_framework import routers
from views import ListNotes
from django.urls import path


urlpatterns = [
    path("notes/", ListNotes.as_view(), name="notes-list"),
]
