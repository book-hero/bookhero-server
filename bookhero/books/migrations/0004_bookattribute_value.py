# Generated by Django 2.1.7 on 2019-04-19 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_userbookattributedescriptor'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookattribute',
            name='value',
            field=models.IntegerField(null=True),
        ),
    ]
