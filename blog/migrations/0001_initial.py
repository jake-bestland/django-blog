# Generated by Django 5.0.7 on 2024-08-06 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('text', models.TextField()),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
