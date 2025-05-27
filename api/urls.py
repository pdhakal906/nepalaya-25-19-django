from rest_framework import routers
from .views import NotesViewset, UploadView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"notes", NotesViewset)


urlpatterns = [
    path("", include(router.urls)),
    path("upload/", UploadView.as_view(), name="upload-file"),
    # path("notes/", ListNotes.as_view(), name="notes-list"),
]


# urlpatterns = [path("", include(router.urls))]
