# Generated by Django 4.0.6 on 2022-08-31 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminApi', '0006_alter_navlink_options_alter_navlink_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='navlink',
            options={'verbose_name': 'menu', 'verbose_name_plural': 'menus'},
        ),
    ]
