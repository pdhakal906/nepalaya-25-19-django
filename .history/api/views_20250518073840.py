from rest_framework.views import APIView
from rest_framework.response import Response
from notes.models import Note


class ListNotes(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all notes.
        """

        notes = Note.objects.all()

        notes = [{"id": note.id, "text": note.text} for note in notes]

        [{"id": 1, "text": "kajsfdkj"}]

        # notes = [note.text for note in Note.objects.all()]
        return Response(notes)
