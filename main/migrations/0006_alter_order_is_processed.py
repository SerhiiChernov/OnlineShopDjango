# Generated by Django 5.0.4 on 2024-05-16 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_processed',
            field=models.BooleanField(default=True),
        ),
    ]
