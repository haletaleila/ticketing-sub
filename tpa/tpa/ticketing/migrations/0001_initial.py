# Generated by Django 3.2.14 on 2023-09-06 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blockId', models.IntegerField()),
                ('blockName', models.CharField(max_length=255)),
                ('cornerPoints', models.ManyToManyField(related_name='blocks_with_corner', to='ticketing.Point')),
                ('linkedPoint', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='block_with_linked', to='ticketing.point')),
                ('vectorPoint', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='block_with_vector', to='ticketing.point')),
            ],
        ),
    ]
