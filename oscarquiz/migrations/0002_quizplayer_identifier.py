# Generated by Django 2.0.2 on 2018-03-04 03:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oscarquiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizplayer',
            name='identifier',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
