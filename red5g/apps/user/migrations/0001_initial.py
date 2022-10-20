# Generated by Django 4.1.2 on 2022-10-20 20:55

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
                ('name', models.CharField(max_length=70)),
                ('mail', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('direction', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=30)),
                ('date', models.DateField()),
            ],
        ),
    ]