from rest_framework import serializers


from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "text"]

    # id = serializers.IntegerField(read_only=True)
    # text = serializers.CharField(max_length=200)
