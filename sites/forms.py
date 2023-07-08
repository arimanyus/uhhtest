from django import forms
from .models import UserWebsite, Template, Site
import os
from django.conf import settings

# You can replace these with your actual choices
INDUSTRY_CHOICES = [
    ('IT', 'Information Technology'),
    ('EC', 'E-commerce'),
    ('ED', 'Education'),
    # add more industries here...
]

COLOR_SCHEME_CHOICES = [
    ('LB', 'Light Blue'),
    ('DB', 'Dark Blue'),
    ('G', 'Green'),
    # add more color schemes here...
]


def get_template_choices():
    templates_path = os.path.join(settings.BASE_DIR, 'sites', 'templates',
                                  'user_templates')
    templates = os.listdir(templates_path)
    return [(template, template) for template in templates]


class WebsiteForm(forms.ModelForm):
    template_name = forms.ChoiceField(choices=get_template_choices())
    industry = forms.ChoiceField(choices=INDUSTRY_CHOICES)
    color_scheme = forms.ChoiceField(choices=COLOR_SCHEME_CHOICES)

    class Meta:
        model = Site
        fields = [
            'template_name', 'description', 'industry', 'logo', 'color_scheme'
        ]
