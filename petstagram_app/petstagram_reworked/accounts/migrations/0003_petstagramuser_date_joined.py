# Generated by Django 3.1.3 on 2022-03-13 19:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_petstagramuser_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='petstagramuser',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]