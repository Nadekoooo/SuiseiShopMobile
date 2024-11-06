from django.db import models
import uuid
from django.contrib.auth.models import User

class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    category = models.TextField()
    