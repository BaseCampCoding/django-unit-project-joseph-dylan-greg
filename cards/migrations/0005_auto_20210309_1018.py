# Generated by Django 3.1.7 on 2021-03-09 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20210309_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionmodel',
            old_name='title',
            new_name='Answer',
        ),
    ]
