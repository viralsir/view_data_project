# Generated by Django 3.1.3 on 2020-11-24 06:49

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
                ('sname', models.CharField(max_length=50)),
                ('maths', models.IntegerField()),
                ('sci', models.IntegerField()),
                ('eng', models.IntegerField()),
            ],
        ),
    ]