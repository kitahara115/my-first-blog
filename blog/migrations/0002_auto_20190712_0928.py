# Generated by Django 2.0.13 on 2019-07-12 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publishde_date',
            new_name='published_date',
        ),
    ]
