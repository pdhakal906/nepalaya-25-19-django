from rest_framework.views import APIView
from rest_framework.response import Response
from notes.models import Note
from .serializer import NoteSerializer, UploadSerializer
import os
from django.conf import settings
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import re
from modules.ocr_engine import extract_text


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


class NotesViewset(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    http_method_names = ["get", "post", "put", "delete", "head", "options", "trace"]


class UploadView(APIView):
    parser_classes = [
        MultiPartParser,
        FormParser,
    ]

    @swagger_auto_schema(request_body=UploadSerializer)
    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        print(request.data)
        # return Response({"message": "File uploaded successfully"})
        uploaded_file = request.data.get("file")

        if uploaded_file:
            save_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
            path = default_storage.save(save_path, ContentFile(uploaded_file.read()))
            print("processing image.....")

            result = extract_text(os.path.join(settings.MEDIA_ROOT, path))
            # print(result)

            extracted_text = ""
            if result["STATUS"] == "SUCCESS":
                extracted_text = result["DATA"]
            # return Response(
            #     {
            #         "file_path": "127.0.0.1:8000/images/"
            #         + re.sub("/upload/", "/", path),
            #         "message": "File uploaded successfully",
            #         "text": extracted_text,
            #         # "tetx": "this is text extracted",
            #     }
            # )
            print(request.build_absolute_uri(path))
            return Response(
                {
                    "file_path": re.sub(
                        "/api/upload/", "/images/", request.build_absolute_uri(path)
                    ),
                    "message": "File uploaded successfully",
                    "text": extracted_text,
                    # "tetx": "this is text extracted",
                }
            )
