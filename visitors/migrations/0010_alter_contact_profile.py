# Generated by Django 3.2.6 on 2021-08-26 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0009_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitors.profile'),
        ),
    ]
