# Generated by Django 3.0.14 on 2023-05-31 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=100)),
                ('sname', models.CharField(max_length=100)),
                ('sage', models.IntegerField()),
                ('sadd', models.CharField(max_length=100)),
            ],
        ),
    ]
