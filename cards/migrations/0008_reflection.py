# Generated by Django 3.1.7 on 2021-03-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_merge_20210310_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reflection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=400)),
            ],
        ),
    ]
