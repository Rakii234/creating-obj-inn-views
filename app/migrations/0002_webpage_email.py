# Generated by Django 4.1.7 on 2023-04-03 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='email',
            field=models.EmailField(default='rocky@gmail.com', max_length=254),
        ),
    ]
