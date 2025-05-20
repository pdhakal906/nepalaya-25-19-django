from rest_framework import routers
from .views import ListNotes, NotesViewset
from django.urls import path
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register(r"notes", NotesViewset)


urlpatterns = [
    path("notes/", ListNotes.as_view(), name="notes-list"),
] + router.urls
