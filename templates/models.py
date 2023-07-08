from django.db import models

LAYOUT_CHOICES = [
    ('default', 'Default'),
    ('two_columns', 'Two Columns'),
    # Add more layout options here
]


class Template(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    preview_image = models.ImageField(upload_to='templates/preview_images/')
    template_file = models.FileField(upload_to='templates/files/')
    layout = models.CharField(max_length=50,
                              choices=LAYOUT_CHOICES,
                              default='default')

    def __str__(self):
        return self.name
