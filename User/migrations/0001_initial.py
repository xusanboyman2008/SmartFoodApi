# Generated by Django 5.1.4 on 2025-01-20 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tg_id', models.IntegerField()),
                ('username', models.CharField(max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
