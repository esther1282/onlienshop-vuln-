# Generated by Django 3.2.13 on 2022-06-14 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_productimage_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='num',
            field=models.IntegerField(default=1),
        ),
    ]
