# Generated by Django 3.2.5 on 2021-07-24 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='profile',
            new_name='avatar_url',
        ),
    ]