# Generated by Django 4.2.6 on 2024-02-09 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='school',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=23)),
                ('sprincipal', models.CharField(max_length=23)),
            ],
        ),
    ]
