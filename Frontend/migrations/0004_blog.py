# Generated by Django 4.2.7 on 2023-12-18 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0003_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
