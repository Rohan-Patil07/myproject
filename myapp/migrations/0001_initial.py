# Generated by Django 4.0.4 on 2022-05-05 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('org_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('org_name', models.CharField(max_length=25)),
                ('org_email', models.EmailField(max_length=254, unique=True)),
                ('org_pw', models.TextField(max_length=100)),
                ('user_status', models.CharField(max_length=8)),
            ],
        ),
    ]