# Generated by Django 3.1.3 on 2022-09-09 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_auto_20220909_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='votor',
            new_name='voter',
        ),
    ]
