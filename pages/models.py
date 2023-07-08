from django.db import models
from templates.models import Template
from ckeditor.fields import RichTextField


class Page(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    slug = models.SlugField(unique=True)
    template = models.ForeignKey(Template,
                                 on_delete=models.SET_NULL,
                                 null=True)

    def __str__(self):
        return self.title
