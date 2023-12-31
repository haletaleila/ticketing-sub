# Generated by Django 3.2.14 on 2023-09-06 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='linkedPoint',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='block_with_linked', to='ticketing.point'),
        ),
        migrations.AlterField(
            model_name='block',
            name='vectorPoint',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='block_with_vector', to='ticketing.point'),
        ),
    ]
