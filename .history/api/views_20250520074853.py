from rest_framework.views import APIView
from rest_framework.response import Response
from notes.models import Note
from .serializer import NoteSerializer

from rest_framework import viewsets


# class ListNotes(APIView):
#     """
#     View to list all users in the system.

#     * Requires token authentication.
#     * Only admin users are able to access this view.
#     """

#     def get(self, request, format=None):
#         """
#         Return a list of all notes.
#         """

#         notes = Note.objects.all().order_by("-id")

#         notes = [{"id": note.id, "text": note.text} for note in notes]

#         # notes = [note.text for note in Note.objects.all()]
#         return Response(notes)


class UploadView(APIView):
    def post(self, request, format=None):
        """
        Upload a file.
        """

        pass


class NotesViewset(viewsets.ModelViewSet):

    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def create(self, request):
        return Response({"message": "Note created successfully!"})

    def update(self, request, pk=None):
        note = Note.objects.get(pk=pk)
        print(request.data)
        note.text = request.data.get("text")
        note.save()
        return Response({"message": "Note updated successfully!"})
