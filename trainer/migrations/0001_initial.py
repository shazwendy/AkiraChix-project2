# Generated by Django 2.2.1 on 2019-05-27 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_joined', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('trainer_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=70)),
                ('phone_number', models.CharField(max_length=15)),
                ('course_teaching', models.CharField(max_length=20)),
            ],
        ),
    ]
