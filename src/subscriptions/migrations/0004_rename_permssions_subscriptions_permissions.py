# Generated by Django 5.0.6 on 2024-07-19 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_subscriptions_permssions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriptions',
            old_name='permssions',
            new_name='permissions',
        ),
    ]
