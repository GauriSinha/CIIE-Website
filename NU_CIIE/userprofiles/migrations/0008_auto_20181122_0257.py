# Generated by Django 2.0 on 2018-11-21 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0007_auto_20181122_0255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='email_confirmed',
            new_name='email_activated',
        ),
    ]