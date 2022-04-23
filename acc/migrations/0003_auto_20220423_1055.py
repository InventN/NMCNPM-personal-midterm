# Generated by Django 3.2.12 on 2022-04-23 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0002_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='acc.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='acc.customer'),
        ),
    ]
