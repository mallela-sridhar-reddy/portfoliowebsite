# Generated by Django 4.2.2 on 2023-06-26 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_project_body_alter_project_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
