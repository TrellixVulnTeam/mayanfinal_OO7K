# Generated by Django 2.2.24 on 2022-03-06 13:39

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0008_theme_background_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='background_menu_dropdown',
            field=colorful.fields.RGBColorField(blank=True, help_text='Color background dropdown menu.', verbose_name='Color background dropdown menu'),
        ),
    ]
