# Generated by Django 5.0.4 on 2024-04-21 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('Suggetion', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
