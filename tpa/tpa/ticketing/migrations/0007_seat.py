# Generated by Django 3.2.14 on 2023-09-08 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0006_block_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logicalSeatId', models.BigIntegerField()),
                ('gradeId', models.IntegerField()),
                ('cornerPoints', models.JSONField()),
                ('position', models.JSONField()),
                ('rowIdx', models.IntegerField()),
                ('colIdx', models.IntegerField()),
                ('mapInfo', models.CharField(max_length=255)),
                ('seatCount', models.IntegerField()),
                ('linkedId', models.IntegerField()),
                ('blockId', models.IntegerField()),
                ('sortMapInfo', models.CharField(max_length=255)),
                ('area', models.JSONField()),
                ('sectionId', models.IntegerField()),
            ],
        ),
    ]
