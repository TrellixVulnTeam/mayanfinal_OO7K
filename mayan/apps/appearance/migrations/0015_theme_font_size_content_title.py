# Generated by Django 2.2.24 on 2022-03-08 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0014_auto_20220308_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='font_size_content_title',
            field=models.IntegerField(default=23, help_text='Font size content title.', verbose_name='Font size content title'),
        ),
    ]
