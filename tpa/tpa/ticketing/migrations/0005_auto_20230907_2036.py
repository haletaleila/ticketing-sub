# Generated by Django 3.2.14 on 2023-09-07 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0004_baseball_eng'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('gradeId', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='baseball',
            name='grade',
            field=models.ManyToManyField(null=True, related_name='baseball_with_grade', to='ticketing.Grade'),
        ),
    ]
