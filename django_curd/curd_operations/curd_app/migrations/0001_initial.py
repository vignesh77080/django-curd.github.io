# Generated by Django 2.2.5 on 2019-09-14 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurdOperations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('age', models.IntegerField(max_length=3)),
                ('dob', models.DateField()),
            ],
        ),
    ]
