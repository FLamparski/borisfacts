from django.db import models

class Story(models.Model):
    # Primary Key
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Public fields
    title = models.CharField(max_length=100)
    content = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, null=True)

    # Admin fields
    author_email = models.EmailField()
    author_email_verified = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
