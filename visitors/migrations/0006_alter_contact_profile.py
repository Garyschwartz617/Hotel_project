# Generated by Django 3.2.6 on 2021-08-26 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visitors', '0005_alter_contact_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_member', to=settings.AUTH_USER_MODEL),
        ),
    ]
