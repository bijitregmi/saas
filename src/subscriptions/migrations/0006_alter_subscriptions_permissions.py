# Generated by Django 5.0.6 on 2024-07-19 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('subscriptions', '0005_alter_subscriptions_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptions',
            name='permissions',
            field=models.ManyToManyField(limit_choices_to={'subcriptions: subscriptions'}, to='auth.permission'),
        ),
    ]