# Generated by Django 2.2.24 on 2022-03-06 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0003_auto_20210823_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='brand_name',
            field=models.CharField(blank=True, help_text='Set text Brand.', max_length=100, verbose_name='Brand name'),
        ),
    ]
