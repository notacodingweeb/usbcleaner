from django.db import models

# Create your models here.
class FileModel(models.Model):
    message_type = models.CharField(max_length=1000)
    filePath = models.CharField(max_length=1000) 
    total_score = models.CharField(max_length=1000) 
    fileType = models.CharField(max_length=1000) 
    fileSize = models.CharField(max_length=1000)
    firstBytesString = models.CharField(max_length=1000)
    hashString = models.CharField(max_length=1000)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message_type


