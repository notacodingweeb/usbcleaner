from rest_framework import serializers
from .models import FileModel


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = ['id', 'message_type','filePath', 'total_score', 'fileType', 'fileSize', 'firstBytesString', 'hashString']