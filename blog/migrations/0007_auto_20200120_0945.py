# Generated by Django 2.0.13 on 2020-01-20 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200116_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='phone_no1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='phone_no2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='phone_no3',
        ),
        migrations.AddField(
            model_name='post',
            name='phone_no',
            field=models.CharField(default=0, max_length=11),
            preserve_default=False,
        ),
    ]
