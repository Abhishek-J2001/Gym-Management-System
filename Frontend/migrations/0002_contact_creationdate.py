# Generated by Django 4.2.7 on 2023-12-03 13:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='creationdate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
