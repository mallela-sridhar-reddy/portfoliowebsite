# Generated by Django 4.2.2 on 2023-06-27 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='created',
            field=models.DateTimeField(null=True),
        ),
    ]