# Generated by Django 5.0.6 on 2024-07-19 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0002_alter_pagevisits_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagevisits',
            options={'verbose_name': 'Page visit'},
        ),
    ]