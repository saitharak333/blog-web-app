# Generated by Django 2.1.5 on 2019-01-07 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='text',
            new_name='body',
        ),
    ]
