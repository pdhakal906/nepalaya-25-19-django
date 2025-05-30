from rest_framework import serializers


from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "text"]


class UploadSerializer(serializers.Serializer):
    file = serializers.FileField()
