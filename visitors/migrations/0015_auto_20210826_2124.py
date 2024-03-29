# Generated by Django 3.2.6 on 2021-08-26 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0014_auto_20210826_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='staff_members',
        ),
        migrations.AddField(
            model_name='contact',
            name='author',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitors.profile'),
        ),
    ]
