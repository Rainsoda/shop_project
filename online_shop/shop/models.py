import uuid

from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200, 
        unique=True
    )

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"])
        ]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
