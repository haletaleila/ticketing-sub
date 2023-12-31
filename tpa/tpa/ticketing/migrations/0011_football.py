# Generated by Django 3.2.14 on 2023-10-04 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0010_baseball_imageurlthumnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Football',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('eng', models.CharField(max_length=255, null=True)),
                ('imageUrlThumnail', models.ImageField(blank=True, null=True, upload_to='ticketing/football/images/')),
                ('blocks', models.ManyToManyField(null=True, related_name='football_with_blocks', to='ticketing.Block')),
                ('grade', models.ManyToManyField(null=True, related_name='football_with_grade', to='ticketing.Grade')),
            ],
        ),
    ]
