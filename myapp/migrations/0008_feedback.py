# Generated by Django 3.2.5 on 2021-08-26 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_contact_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=122)),
                ('feedback', models.CharField(max_length=150)),
                ('suggestion', models.CharField(max_length=150)),
            ],
        ),
    ]
