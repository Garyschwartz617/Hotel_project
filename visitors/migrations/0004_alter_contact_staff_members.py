# Generated by Django 3.2.6 on 2021-08-26 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0003_alter_contact_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='staff_members',
            field=models.ManyToManyField(blank=True, related_name='staff_member', to='visitors.Profile'),
        ),
    ]
