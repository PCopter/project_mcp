# Generated by Django 5.0.4 on 2024-05-08 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_general', '0004_remove_subscription_certification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='status',
            field=models.CharField(choices=[('unapproved', 'Unapproved'), ('approved', 'Approved'), ('banned', 'Banned')], default='unapproved', max_length=15),
        ),
    ]
