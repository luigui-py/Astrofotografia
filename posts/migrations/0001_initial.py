# Generated by Django 3.2.6 on 2021-09-29 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=12)),
                ('bio', models.TextField()),
                ('birthday', models.DateField()),
            ],
        ),
    ]
