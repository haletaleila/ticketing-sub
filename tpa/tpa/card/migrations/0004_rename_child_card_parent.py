# Generated by Django 3.2.14 on 2023-09-20 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_auto_20230920_2155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='child',
            new_name='parent',
        ),
    ]