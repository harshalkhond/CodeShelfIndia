# Generated by Django 3.2.5 on 2021-08-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_contact_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='feedback',
            field=models.CharField(default='Feedback', max_length=50),
        ),
    ]