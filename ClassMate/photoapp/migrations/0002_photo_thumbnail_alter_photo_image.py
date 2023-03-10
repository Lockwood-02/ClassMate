# Generated by Django 4.1.6 on 2023-03-05 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='thumbnail',
            field=models.ImageField(default=models.FileField(upload_to='photos/'), upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.FileField(upload_to='photos/'),
        ),
    ]
