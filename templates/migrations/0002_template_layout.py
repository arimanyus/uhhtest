# Generated by Django 3.2.13 on 2023-05-15 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='layout',
            field=models.CharField(choices=[('default', 'Default'), ('two_columns', 'Two Columns')], default='default', max_length=50),
        ),
    ]
