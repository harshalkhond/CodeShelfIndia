# Generated by Django 3.2.5 on 2022-02-03 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_remove_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='username',
            field=models.CharField(default='username', max_length=30),
        ),
    ]
