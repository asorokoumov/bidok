# Generated by Django 2.2.2 on 2019-06-28 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0007_order_logist'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='comment',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
