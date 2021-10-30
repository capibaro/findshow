# Generated by Django 3.2.4 on 2021-10-28 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('url', models.URLField(max_length=50)),
                ('date', models.CharField(max_length=30)),
                ('time', models.DateTimeField()),
                ('venue', models.TextField()),
                ('artist', models.TextField()),
                ('post', models.URLField(max_length=255)),
                ('source', models.CharField(max_length=10)),
            ],
        ),
    ]
