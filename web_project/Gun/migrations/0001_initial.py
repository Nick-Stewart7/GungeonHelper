# Generated by Django 3.2.7 on 2021-09-17 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gunName', models.TextField()),
                ('quote', models.TextField()),
                ('type', models.TextField()),
                ('DPS', models.TextField()),
                ('mag', models.TextField()),
                ('ammo', models.TextField()),
                ('rate', models.TextField()),
                ('reload', models.TextField()),
                ('shotspd', models.TextField()),
                ('range', models.TextField()),
                ('force', models.TextField()),
                ('spread', models.TextField()),
            ],
        ),
    ]
