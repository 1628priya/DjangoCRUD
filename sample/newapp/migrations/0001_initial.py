# Generated by Django 4.0.2 on 2022-11-02 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('registration_code', models.CharField(max_length=5)),
                ('chancellor', models.CharField(max_length=50)),
            ],
        ),
    ]
