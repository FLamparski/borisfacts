import uuid
from datetime import datetime
from django.db import models

class Story(models.Model):
    class Meta:
        verbose_name_plural = 'stories'

    # Primary Key
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Public fields
    title = models.CharField(max_length=100)
    content = models.TextField()
    submitted_at = models.DateTimeField(default=datetime.now)
    author = models.CharField(max_length=100, null=True)

    # Admin fields
    author_email = models.EmailField()
    author_email_verified = models.BooleanField(default=False, editable=False)
    email_verification_code = models.UUIDField(default=uuid.uuid4, null=True, editable=False)
    published = models.BooleanField(default=False)

    # Additional methods
    def __str__(self):
        return self.title
