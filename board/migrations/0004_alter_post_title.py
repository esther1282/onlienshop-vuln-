# Generated by Django 3.2.13 on 2022-07-20 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_rename_user_post_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(max_length=50),
        ),
    ]