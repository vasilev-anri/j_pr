# Generated by Django 4.0.1 on 2022-01-25 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_job_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='company_logos'),
        ),
    ]
