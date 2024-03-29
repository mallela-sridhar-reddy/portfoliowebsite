# Generated by Django 4.2.2 on 2023-06-27 07:30

import ckeditor_uploader.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_project_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('subject', models.CharField(max_length=500, null=True)),
                ('body', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
