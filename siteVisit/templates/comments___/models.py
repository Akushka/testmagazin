from django.db import models
from django_comments.models import CommentAbstractModel

class CommentWithTitle(CommentAbstractModel):
    title = models.CharField(max_length=300)