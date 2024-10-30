import uuid
from django.db import models

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Translation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='translations')
    language = models.CharField(max_length=50)  # e.g., "English", "Arabic", "French"
    translator = models.CharField(max_length=100, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    is_original = models.BooleanField(default=False)  # Field to mark the original version

    def __str__(self):
        version = "Original" if self.is_original else self.language
        return f"{self.book.title} - {version}"

class ContentSection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    translation = models.ForeignKey(Translation, on_delete=models.CASCADE, related_name='content_sections')
    index = models.CharField(max_length=100)
    sub_index = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    page_number = models.PositiveIntegerField()

    class Meta:
        ordering = ['page_number']

    def __str__(self):
        return f"{self.translation.book.title} ({self.translation.language}) - {self.index} - {self.sub_index or 'No Sub Index'}"
