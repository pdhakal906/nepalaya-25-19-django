from rest_framework import routers
from .views import NotesViewset
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"notes", NotesViewset)


urlpatterns = [
    # path("notes/", ListNotes.as_view(), name="notes-list"),
] + router.urls
