# Generated by Django 3.1.6 on 2021-03-23 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duoclieu', '0010_auto_20210323_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level0',
            name='noi_dung',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='mục tiêu'),
        ),
    ]
